# Setup and Install
# Run these commands in the terminal before running the app
# pip3 install pipenv
# pipenv --version
# export PIPENV_IGNORE_VIRTUALENVS=1
# pipenv install
# pipenv install streamlit
# pipenv run streamlit run app.py

# Streamlit App Code

import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import time

# Title and Text Elements
st.title("Streamlit Basics")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")
st.write("This is a write dimension")
st.markdown("[Streamlit](https://www.streamlit.io)")

# HTML Section
html_page = '''
<div style="background-color:blue;padding: 50px">
<p style="color:yellow; font-size:50px">Enjoy Streamlit!</p>
</div>
'''
st.markdown(html_page, unsafe_allow_html=True)

# Status Messages
st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

# Image
# Uncomment and replace "packt.jpeg" with a valid path if you have the image
# img = Image.open("packt.jpeg")
# st.image(img, width=300, caption="Packt Logo")

# Video (from file and YouTube)
# video_file = open("SampleVideo_1280x720_1mb.mp4", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

# st.video("https://www.youtube.com/watch?v=q2EqJW8VzJ0")

# Audio
# audio_file = open("sample1.mp3", "rb")
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format="audio/mp3")

# Widgets
st.header("Widgets")

if st.button("Play"):
    st.text("Hello world!")

if st.checkbox("Checkbox"):
    st.text("Checkbox selected")

radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
    st.info("You selected A")
else:
    st.info("You selected B")

city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])
occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])
name = st.text_input("Your Name", "Write something...")
st.text(name)
age = st.number_input("Input a number")
message = st.text_area("Your Message", "Write something...")
select_val = st.slider("Select a Value", 1, 10)

if st.button("Balloons"):
    st.balloons()

# DataFrames and Charts
st.header("Dataframes and Tables")
# Uncomment the below line and ensure 'auto.csv' is in your directory
# df = pd.read_csv("auto.csv")
# st.dataframe(df.head(10))
# st.table(df.head(10))
# st.area_chart(df[["mpg", "cylinders"]])
# st.bar_chart(df[["mpg", "cylinders"]].head(20))
# st.line_chart(df[["mpg", "cylinders"]].head(20))

# Correlation Heatmap
# fig, ax = plt.subplots()
# corr_plot = sns.heatmap(df[["mpg", "cylinders", "displacement"]].corr(), ax=ax)
# st.pyplot(fig)

# Date and Time
today = st.date_input("Today is", datetime.datetime.now())
hour = st.time_input("The time is", datetime.time(12, 30))

# JSON and Code
data = {"name": "John", "surname": "Wick"}
st.json(data)
st.code("import pandas as pd")

julia_code = """
function doit(num::Int)
    println(num)
end
"""
st.code(julia_code, language='julia')

# Math and Markdown
st.latex(r"\alpha^2 + \beta^2 = \gamma^2")
st.markdown("This is a markdown cell")

# Progress Bar
my_bar = st.progress(0)
for value in range(100):
    time.sleep(0.1)
    my_bar.progress(value + 1)