import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.parse

def scrape_multiple_categories(categories, output_csv, pages_per_category=10):
    """
    Scrape articles from The Hindu for multiple categories and combine them into a single CSV file.
    
    Args:
        categories (list): List of category search terms
        output_csv (str): Path to the output CSV file
        pages_per_category (int): Number of pages to scrape per category
    
    Returns:
        DataFrame: Combined dataset of all scraped articles
    """
    # Initialize a list to store all DataFrames
    all_dfs = []
    
    # Set up Selenium to handle JavaScript-loaded content
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    # Initialize the driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Process each category
        for category in categories:
            print(f"\n{'='*50}")
            print(f"STARTING CATEGORY: {category}")
            print(f"{'='*50}\n")
            
            # URL encode the category for the search
            encoded_category = urllib.parse.quote(category)
            
            # Initialize lists to store data for this category
            titles, subtitles, authors, contents, article_urls = [], [], [], [], []
            
            # Loop through pages for this category
            for page_number in range(1, pages_per_category + 1):
                print(f"Scraping {category} - Page {page_number}...")
                
                # Construct the URL for the search results page
                search_url = f"https://www.thehindu.com/search/#gsc.tab=0&gsc.q={encoded_category}&gsc.sort=&gsc.page={page_number}"
                
                try:
                    # Load the page with Selenium
                    driver.get(search_url)
                    
                    # Wait for the search results to load
                    WebDriverWait(driver, 20).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "gsc-expansionArea"))
                    )
                    
                    # Add a short delay to ensure all results are loaded
                    time.sleep(5)
                    
                    # Get the page source after JavaScript has run
                    page_source = driver.page_source
                    soup = BeautifulSoup(page_source, "html.parser")
                    
                    # Find the expansion area that contains all results
                    expansion_area = soup.find("div", class_="gsc-expansionArea")
                    
                    if not expansion_area:
                        print("Could not find expansion area. Page structure might have changed.")
                        continue
                    
                    # Find all result items
                    result_items = expansion_area.find_all("div", class_="gsc-webResult gsc-result")
                    print(f"Found {len(result_items)} result items on page {page_number}")
                    
                    article_links = []
                    
                    for item in result_items:
                        # Navigate through the nested structure
                        gs_web_result = item.find("div", class_="gs-webResult gs-result")
                        if gs_web_result:
                            thumbnail_inside = gs_web_result.find("div", class_="gsc-thumbnail-inside")
                            if thumbnail_inside:
                                gs_title_div = thumbnail_inside.find("div", class_="gs-title")
                                if gs_title_div:
                                    gs_title_link = gs_title_div.find("a", class_="gs-title", href=True)
                                    if gs_title_link and 'href' in gs_title_link.attrs:
                                        link = gs_title_link['href']
                                        if 'thehindu.com' in link and link not in article_links:
                                            article_links.append(link)
                    
                    print(f"Found {len(article_links)} article links on page {page_number}")
                    
                    # Scrape each article link
                    for article_url in article_links:
                        try:
                            # Request the article page
                            article_response = requests.get(article_url)
                            article_soup = BeautifulSoup(article_response.content, "html.parser")
                            
                            # Extract title, subtitle, and author
                            title = article_soup.find("h1", class_="title").text.strip() if article_soup.find("h1", class_="title") else "No Title"
                            subtitle = article_soup.find("h2", class_="sub-title").text.strip() if article_soup.find("h2", class_="sub-title") else "No Subtitle"
                            author = article_soup.find("a", class_="person-name lnk").text.strip() if article_soup.find("a", class_="person-name lnk") else "Miscellaneous"
                            
                            # Extract content (from the first two <p> tags inside specific div)
                            content = ""
                            content_div = article_soup.find("div", class_=["articlebodycontent", "col-xl-9 col-lg-12 col-md-12 col-sm-12 col-12"])
                            if content_div:
                                paragraphs = content_div.find_all("p", limit=2)
                                content = " ".join([p.text.strip() for p in paragraphs])
                            
                            combined_content = f"{title} {subtitle} {content}"
                            
                            # Append data to lists
                            titles.append(title)
                            subtitles.append(subtitle)
                            authors.append(author)
                            contents.append(combined_content)
                            article_urls.append(article_url)
                            
                            print(f"Scraped article: {title}")
                            
                            # Add a small delay to avoid hitting the server too hard
                            time.sleep(1)
                            
                        except Exception as e:
                            print(f"Failed to scrape {article_url}: {e}")
                    
                    # Add a delay between pages
                    time.sleep(2)
                    
                except Exception as e:
                    print(f"Failed to scrape page {page_number}: {e}")
            
            # Create a DataFrame for this category
            if titles:  # Check if we have any data
                data = {
                    'title': titles,
                    'subtitle': subtitles,
                    'author': authors,
                    'content': contents,
                    'link': article_urls,
                    'category': [category] * len(titles)  # Add the category to all rows
                }
                
                category_df = pd.DataFrame(data)
                all_dfs.append(category_df)
                
                print(f"Completed category: {category} - {len(titles)} articles collected")
            else:
                print(f"No articles found for category: {category}")
    
    finally:
        # Close the Selenium driver
        driver.quit()
    
    # Combine all DataFrames
    if all_dfs:
        combined_df = pd.concat(all_dfs, ignore_index=True)
        
        # Add unique_id column
        combined_df['unique_id'] = combined_df.index + 1
        
        # Save the combined dataset to CSV
        combined_df.to_csv(output_csv, index=False, encoding='utf-8')
        print(f"\nCombined dataset saved as '{output_csv}' with {len(combined_df)} total articles.")
        return combined_df
    else:
        print("No data was collected for any category. Please check the website structure or search terms.")
        return pd.DataFrame()

# Example usage
if __name__ == "__main__":
    # List of categories to scrape
    categories = [
        "climate change",
        "carbon footprint",
        "sustainable living",
        "green technology",
        "renewable energy",
        "eco-friendly living"
    ]
    
    output_csv = "thehindu_environmental_articles_combined.csv"
    
    # Scrape all categories and combine results
    combined_df = scrape_multiple_categories(categories, output_csv, pages_per_category=5)