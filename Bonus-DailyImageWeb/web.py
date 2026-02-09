import streamlit as st
import requests

#getting api key and url
api_key = "xm4btTh5pbGPnk4jDV2N6upjLPF3kntJQ2O4GoES"
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

#creating request the information about url and data
request = requests.get(url)
data = request.json()

#using data in url with json file.
exp = data['explanation']
title = data['title']
img_url = data['url']
date = data['date']

#download image in data
filepath = "img.png"
content2 = requests.get(img_url)
with open(filepath, "wb") as file:
    file.write(content2.content)

#streamlit gui creations
st.text(date)
st.header(title)
st.image(filepath)
st.text(exp)
