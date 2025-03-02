import streamlit as st
import folium # type: ignore
from streamlit_folium import folium_static # type: ignore

# Conversion factor: 1 metric ton (1000 kg) CO₂ = 0.3 hectares lost
CO2_TO_FOREST_LOSS_HA = 0.0003  # per kg CO₂

def co2_to_forest_area(co2_kg):
    """Convert CO₂ footprint (kg) to forest area lost (hectares & square meters)."""
    lost_area_ha = co2_kg * CO2_TO_FOREST_LOSS_HA  # Convert kg to hectares
    lost_area_m2 = lost_area_ha * 10000  # Convert hectares to square meters
    return lost_area_m2

def generate_polygon(center_lat, center_lon, area_m2):
    """Generate a square polygon covering the lost forest area."""
    side_length = (area_m2 ** 0.5) / 111320  # Convert meters to degrees (approx)
    
    lat_min = center_lat - side_length / 2
    lat_max = center_lat + side_length / 2
    lon_min = center_lon - side_length / 2
    lon_max = center_lon + side_length / 2
    
    return [(lat_min, lon_min), (lat_min, lon_max), (lat_max, lon_max), (lat_max, lon_min), (lat_min, lon_min)]

# 🎨 Streamlit UI
st.title("🌿 CO₂ Footprint & Forest Loss Visualizer")
st.markdown("See how your carbon emissions contribute to deforestation.")

# 📌 User Input
co2_kg = st.number_input("Enter CO₂ footprint (kg):", min_value=1, value=1000, step=10)

# 🌍 Default Location (Amazon Rainforest)
default_location = (-3.4653, -62.2159)  
latitude = st.number_input("Enter Latitude:", value=default_location[0], format="%.6f")
longitude = st.number_input("Enter Longitude:", value=default_location[1], format="%.6f")

if st.button("Visualize Impact"):
    lost_area_m2 = co2_to_forest_area(co2_kg)
    polygon_coords = generate_polygon(latitude, longitude, lost_area_m2)
    
    # 🗺️ Force extreme zoom-in (so the polygon looks big)
    zoom_level = 18  # 👈 Maximum close-up zoom for strong impact!

    # 🗺️ Create Folium Map with forced close-up zoom
    m = folium.Map(location=[latitude, longitude], zoom_start=zoom_level)

    # 🟩 Draw Forest Loss Polygon
    folium.Polygon(
        locations=polygon_coords,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.5,
        popup=f"Forest Loss: {lost_area_m2:.2f} m²",
    ).add_to(m)

    # 🖥️ Display Map in Streamlit
    folium_static(m)
