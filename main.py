import streamlit as st
import requests
import os

# Build API key and url
api_key = os.getenv("API_KEY_ASTRONOMY_IMAGE")
url = "https://api.nasa.gov/planetary/apod?"\
      f"api_key={api_key}"

# Request API data
request = requests.get(url)
content = request.json()

# Download image
img_url = content["url"]
response = requests.get(img_url)
with open("image.jpg", "wb") as file:
    file.write(response.content)

# Build webpage
st.title(content["title"])
st.image("image.jpg")
st.write(content["explanation"])
