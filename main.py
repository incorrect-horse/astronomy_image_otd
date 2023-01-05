import streamlit as st
import requests

# Build API key and url
api_key = "Y5P8FcxRi0RMvYK5xyMgd0ipUVSETPpCDl8yFxrE"
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
