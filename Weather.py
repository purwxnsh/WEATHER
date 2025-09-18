import streamlit as st
import requests
from datetime import datetime
from PIL import Image
import io


st.set_page_config(
    page_title="WEATHER PROJECT | Major Project",
    page_icon="✨",
    layout="centered")

st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        .main {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(15px);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0px 10px 25px rgba(0,0,0,0.4);
        }
        h1, h2, h3, h4 {
            color: #ffdd59;
            text-align: center;
        }
        .card {
            background: rgba(255,255,255,0.15);
            padding: 20px;
            margin: 10px 0;
            border-radius: 15px;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.3);
        }
        .stTextInput, .stSelectbox, .stButton>button, .stDownloadButton>button {
            border-radius: 12px;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        }
        .stButton>button {
            background: linear-gradient(135deg, #00ff99, #00ccff);
            color: black;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            transform: scale(1.07);
            box-shadow: 0px 6px 20px rgba(0,0,0,0.6);
        }
        .stDownloadButton>button {
            background: linear-gradient(135deg, #ff9966, #ff5e62);
            color: white;
            font-weight: bold;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            color: #ddd;
            font-size: 14px;
        }
        .brand {
    color: #FF0000;
    font-weight: bold;
    animation: glow 1.5s ease-in-out infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 5px #FF0000, 0 0 10px #FF0000; }
    to { text-shadow: 0 0 20px #FF0000, 0 0 30px #FF0000; }
}


    </style>
""", unsafe_allow_html=True)

st.title("🌦 Weather Dashboard")

city = st.text_input("Enter city name", "Kharar")

if st.button("Get Weather"):
    api_key = "YOUR_API_KEY"  # <-- Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Current weather
        current = data['list'][0]
        temp = current['main']['temp']
        desc = current['weather'][0]['description']
        st.subheader(f"🌍 Current Weather in {city}")
        st.write(f"**Temperature:** {temp} °C")
        st.write(f"**Condition:** {desc.title()}")
        
        # Forecast
        st.subheader("📅 5-Day Forecast")
        for forecast in data['list'][::8]:  # every 8th entry = 24 hrs
            dt = datetime.fromtimestamp(forecast['dt']).strftime("%d %b %Y")
            temp = forecast['main']['temp']
            desc = forecast['weather'][0]['description']
            st.write(f"**{dt}:** {temp} °C, {desc.title()}")
    else:
        st.error("❌ City not found or API error")

st.markdown("<footer>© 2025 Weather App Project | <span class='brand'>Design by PURWANSH CHAUDAHRY</span> | Made with ❤️ in Python & Streamlit</footer>", unsafe_allow_html=True)
