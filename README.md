# 🌍 Eco-X: Your Personal Climate Companion  

> *"The greatest threat to our planet is the belief that someone else will save it."* – Robert Swan  

Hey there, eco-warrior! Ever wondered how much impact your daily choices have on the environment?  
From the food you eat 🍽️ to the way you travel 🚗, every decision adds up.  
**But don’t worry, Eco-X is here to help!**  


![Screenshot 2025-03-02 164457](https://github.com/user-attachments/assets/98b53b67-60af-495e-b2cd-fe2ef2d33287)

## 🚀 What is Eco-X?  
Eco-X is a **next-gen carbon footprint tracker** designed to make sustainability more than just numbers on a screen.  
It’s an **engaging, insightful, and action-driven** platform that helps you:  

✅ **Track** your daily carbon footprint 📊  
✅ **Understand** its impact on forests 🌳  
✅ **Get insights** from environmental news & blogs 📰  
✅ **Generate reports** with in-depth sustainability research 📜  
✅ **Receive personalized suggestions** for improvement 💡  

## 🌱 Why Choose Eco-X?  

### 🚗 **Track Your Daily Footprint**  
- 📱 Monitor your environmental impact through an intuitive tracking system.  
- 🍽️ Input diet choices, energy consumption, and more!  
- 🌵 Visualize your carbon footprint’s effect on the environment.  
- 💡 Get personalized recommendations to improve your sustainability journey.  

### 📈 **Become Aware of the Consequences**  
- 📰 Browse the latest environmental news from credible sources.  
- 🌿 Choose across multiple categories for tailored insights.  
- 🔄 Access real-time articles and blogs.  
- 🏆 Gain the knowledge to **make informed decisions** about your impact on the planet.  

### 🔍 **Draft Reports & Generate Insights**  
- 🔎 Ask climate-related questions and get AI-powered responses.  
- 🌱 Access the latest sustainability research.  
- 📜 Convert findings into well-structured, downloadable reports.  
- 🤝 Share insights for educational, research, or advocacy purposes.  

## 🔥 What Makes Eco-X Different?  

Let’s be honest. **Most carbon footprint trackers are just… numbers.** 📊  

💀 **Dull visuals.**  
💀 **Temporary engagement.**  
💀 **Over-reliance on gamification & leaderboards.**  

But **are numeric results always effective?** 🤔  
And **should sustainability really be a competition?** 🚫🏆  

### ❌ The Problem  
Most platforms offer **fleeting engagement**—they **quantify but don’t connect.**  
They make users **compete**, when the real challenge is **self-improvement.**  

### ✅ The Eco-X Approach  
✔ **Transforms abstract numbers into visual impact** 🌍  
✔ **Creates an emotional connection to drive real action** ❤️  
✔ **Provides self-improvement tools rather than competition** 🛠️  
✔ **Generates personalized textual insights & reports** 📄  
✔ **Aggregates news, blogs & resources for climate awareness** 🌱  

🌟 **Eco-X isn’t just about numbers—it’s about making sustainability personal, emotional, and actionable.**  

---

## 📌 About Page  

The **About Page** sets the stage for Eco-X, introducing users to the platform with **visually appealing animations and an intuitive layout.**  


### 🛠️ Technologies Used  
- **Streamlit** 🎨 – Powers the entire app, making it interactive and user-friendly.  
- **Lottie Animations** 🎥 – Enhances the experience with smooth, engaging visuals.  
- **Canva** 🖌️ – Used to design the **Eco-X** logo and ensure a polished UI.  

### 🖥️ Features  
✅ **Elegant Layout:** A structured page with **headers, sidebars, and sections** for easy navigation.  
✅ **Dynamic Visuals:** Lottie animations bring the page to life, making climate awareness **engaging and fun.**  
✅ **Mission Statement:** A compelling introduction to **why Eco-X exists** and how it empowers users.  
✅ **User Guidance:** Clear directions on how to use Eco-X, ensuring a smooth experience for first-time visitors.  

🎯 **Goal:**  
Make sustainability **accessible, informative, and visually compelling** from the moment a user enters Eco-X.  

---
## 🌍 FEATURE 1: Carbon Footprint Calculator  

The **Carbon Footprint Calculator** is the core of **Eco-X**, allowing users to estimate their environmental impact based on their daily activities. By inputting data across multiple categories, users get a **detailed report** on their carbon emissions and **actionable insights** to reduce their footprint.  

![Screenshot 2025-03-02 164619](https://github.com/user-attachments/assets/fda4c2d5-bfef-4b38-89b2-81ffbdc9bf21)



### 🎨 Fun Technologies Explored  
From **interactive Folium maps** to **engaging Lottie animations** and **dynamic GIFs**, Eco-X blends **data and visuals** to make carbon footprint tracking both **insightful and exciting!** 🌍✨  


### 🏠 Categories Considered  
To ensure accuracy, the calculator takes user inputs across **five key areas:**  

✅ **Personal Information** – Basic details to personalize results.  
✅ **Home Energy** – Electricity, fuel, and renewable energy usage.  
✅ **Transportation** – Fuel consumption, vehicle type, and travel habits.  
✅ **Consumption & Waste** – Diet, shopping habits, and waste management.  
✅ **Social Activity** – Lifestyle choices that affect carbon emissions.  

---

## ⚙️ Model Training & Selection  

The **carbon footprint estimation model** was trained using **Random Forest** and **XGBoost**, with extensive hyperparameter tuning to achieve high accuracy.  

### 🔬 Hyperparameter Tuning  

#### 🔥 **XGBoost Parameters:**  
XGBoost was tuned using the following **hyperparameters** to optimize model accuracy:  

```python
xg_params = {
    'n_estimators': [100, 200],  # Number of trees in the model
    'learning_rate': [0.05, 0.1],  # Controls step size during boosting
    'max_depth': [3, 6],  # Maximum depth of trees
    'subsample': [0.8, 1.0]  # Fraction of samples used per tree
}
```
#### 🔥 **Random Forest Parameters:**  

```python
rf_params = {
    'n_estimators': [100, 200],  # Number of decision trees
    'max_depth': [None, 10, 20],  # Tree depth for better generalization
    'min_samples_split': [2, 5],  # Minimum samples needed to split a node
    'min_samples_leaf': [1, 2]  # Minimum samples required at leaf node
}
```

## 📊 Performance Comparison  

The **Carbon Footprint Estimation Model** was trained using **XGBoost** and **Random Forest**. Below is the comparison of their performance based on **Root Mean Squared Error (RMSE):**  

| Model          | RMSE (Lower is Better) | Performance |
|---------------|----------------------|-------------|
| **XGBoost**   | **141**               | ✅ Best Accuracy |
| **Random Forest** | **250**           | ❌ Less Accurate |

### 🚀 Why XGBoost?  
XGBoost was selected as the **final model** because:  
✔️ It had a significantly **lower RMSE** than Random Forest.  
✔️ It handles **large datasets efficiently** and prevents overfitting.  
✔️ It **learns better patterns** through boosting, making it ideal for numerical estimations like carbon footprint calculations.  

## 📜 Carbon Impact Report  

After calculating the user's estimated **carbon footprint**, Eco-X generates a **detailed impact report** that goes beyond just numbers.  

### 🌍 What Does the Report Include?  

1️⃣ **📏 CO₂ to Environmental Impact Conversion**  
   - The estimated **CO₂ emissions** are converted into **real-world impact metrics**:  
     - 🌊 **Projected Sea Level Rise** based on CO₂ emissions.  
     - 🌳 **Deforestation Estimate** – The equivalent number of **trees lost annually** due to emissions.  

2️⃣ **🗺️ Forest Map Visualization**  
   - Users can visualize their footprint’s effect on real forests using **Folium Maps**.  
   - Two forests are included for impact projection:  
     - **Birik Forest**, West Bengal, India  
     - **Berambadi State Forest**, Karnataka, India  
   - The map dynamically **zooms in** to show the proportion of forest cleared based on the user's emissions.  

3️⃣ **📊 Interactive Report Elements**  
   - **Lottie Animations** enhance the visual appeal of the report.  
   - The impact is **visually represented** through **graphs, charts, and animations**.  

4️⃣ **💡 AI-Powered Suggestions**  
   - The report leverages **Gemini 2.0 Flash Model** to analyze the user's footprint.  
   - Provides **personalized recommendations** for reducing emissions based on individual lifestyle choices.  

### 🎯 Why This Matters?  
🚀 Instead of just showing numbers, the report **transforms raw data into actionable insights** that users can easily understand and apply!  

---

## 📰 FEATURE 2:  Enhance Your Awareness  

Staying informed is key to making sustainable choices. **Eco-X** helps users **stay up to date** with the latest environmental news through **automated web scraping** and **live search results**.  

![Screenshot 2025-03-02 164642](https://github.com/user-attachments/assets/265a80e0-ff00-4972-ba57-ac2d147d1505)

### 🏛️ Trusted News Source  
- Articles are scraped from **The Hindu**, one of the most **reliable and respected** news platforms in India, using **BeautifulSoup**.  

### 🔍 Explore Topics of Interest  
Users can **choose from various categories** to find news relevant to their interests:  

| Category | Emoji |  
|----------|--------|  
| Climate Change | 🌡️ |  
| Carbon Footprint | 👣 |  
| Sustainable Living | ♻️ |  
| Green Technology | 🔋 |  
| Renewable Energy | 🌞 |  
| Eco-Friendly Living | 🌱 |  

### 🏷️ Dual-Tab Information Display  

📌 **Tab 1: Latest News Articles**  
- Displays **30 popular articles** scraped directly from **The Hindu**.  
- Each article includes a **headline, summary, and direct link** to the full article.  
- Users can **click to visit the original news source** for further reading.  

📌 **Tab 2: Top 10 Google Search Results**  
- Fetches **top 10 real-time searches** under the selected category using the **Google Search API**.  
- Provides **snippets & direct links** for easy access.  

### 🌍 Why This Matters?  
📢 This feature ensures that users are always aware of **real-world climate developments**, helping them **stay informed and take action** in meaningful ways!  

--- 

## 📝 FEATURE 3: Query and Report: Your Personal Research Assistant  

Ever wished for a **custom, well-structured report** on a climate-related topic without the hassle of endless searching? **Eco-X** has you covered!  

![Screenshot 2025-03-02 164718](https://github.com/user-attachments/assets/3d642505-c7bc-4679-bf7e-19cd8a69b1d7)

### 🔍 How It Works  
- **🎤 Speak or Type** – Ask your climate-related question via text or voice input.  
- **🎭 Customize the Report** – Choose the **tone**, **word limit**, and **format** that suits your needs.  
- **🌎 Smart Research** – Leverages **Gemini 2.0 Flash** with **Google Search API** to fetch **reliable and relevant resources**.  
- **📄 Export with Ease** – Download the report in **DOC or PDF formats** or **copy-paste** directly from the app!  

### 🤖 Why **Gemini 2.0 Flash**?  
- **💰 Free to Use** – Unlike other LLMs that require API credits, Gemini is accessible to everyone.  
- **🧠 Smart & Contextual** – Generates well-structured, coherent reports with minimal hallucination.  

### 🔗 Why **Google Search API**?  
- **✅ Ensures Legitimate Links** – Many LLM-generated links are non-functional, but Google's search results **guarantee reliability**.  
- **🌐 Fetches the Latest Info** – Keeps reports **up-to-date with current articles, research, and credible sources**.  

With **Eco-X**, you don’t just get information—you get a **tailored, insightful, and credible report** that’s **ready to use!** 🚀📜  

---


👀 **Ready to take charge of your footprint?**  
Start using **Eco-X** today! 🚀  
