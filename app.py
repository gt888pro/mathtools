from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain

# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
LOTTIE_CUBE_ANIMATION = ASSETS / "cube.json"

# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


# Function to apply snowfall effect
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")


# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]




# Page configuration
st.set_page_config(page_title="Main Page", page_icon="🎄")

# Run snowfall animation
#run_snow_animation()

# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    

# Display header with personalized name
st.header(f"Welcome to my domain!", anchor=False)


# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_CUBE_ANIMATION)
st_lottie(lottie_animation, key="lottie-cube", height=300)

# Personalized holiday message
st.markdown(
    f"Test Website 🌟"
)


    
