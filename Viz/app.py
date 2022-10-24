import streamlit as st
from PIL import Image

# page layout
st.set_page_config(
    page_title = "Global SoMN",
    page_icon = "🌍",
    layout = "wide",
    initial_sidebar_state = "expanded"
)

# page title
st.title("🌍 Global SoMN")
st.subheader("SoMN - Speed of Mobile Network")

# sidebar features
st.sidebar.subheader("Metrics")
with st.sidebar:
    year = st.radio(
        "Year",
        ("2020", "2021")
    )
with st.sidebar:
    season = st.radio(
        "Season",
        ("S1", "S2", "S3", "S4")
    )
with st.sidebar:
    options = st.radio(
    "Select a metric to evaluate",
        (
            "Avg. Upload Speed",
            "Avg. Download Speed",
            "Number of devices",
            "Avg. Latency (ms)"
        )
    )

# display map data
if year == "2020":
    if season == "S1":
        if options == "Avg. Upload Speed":
            image = Image.open('./2020_1/Avg. U 2020_1.png')
            st.image(image, caption='Avg. U 2020_1')
        if options == "Avg. Download Speed":
            image = Image.open('./2020_1/Avg. D 2020_1.png')
            st.image(image, caption='Avg. D 2020_1')
        if options == "Number of devices":
            image = Image.open('./2020_1/# of Devices_2020_1.png')
            st.image(image, caption='# of Devices 2020_1')
        if options == "Avg. Latency (ms)":
            image = Image.open('./2020_1/Avg. Lat Ms_2020_1.png')
            st.image(image, caption='Avg. Lat Ms 2020_1')
    if season == "S2":
        if options == "Avg. Upload Speed":
            image = Image.open('./2020_2/Avg. U 2020_2.png')
            st.image(image, caption='Avg. U 2020_2')
        if options == "Avg. Download Speed":
            image = Image.open('./2020_2/Avg. D 2020_2.png')
            st.image(image, caption='Avg. D 2020_2')
        if options == "Number of devices":
            image = Image.open('./2020_2/# of Devices_2020_2.png')
            st.image(image, caption='# of Devices 2020_2')
        if options == "Avg. Latency (ms)":
            image = Image.open('./2020_2/Avg. Lat Ms 2020_2.png')
            st.image(image, caption='Avg. Lat Ms 2020_2')
    if season == "S3":
        if options == "Avg. Upload Speed":
            image = Image.open('./2020_3/Avg. U 2020_3.png')
            st.image(image, caption='Avg. U 2020_3')
        if options == "Avg. Download Speed":
            image = Image.open('./2020_3/Avg. D 2020_3.png')
            st.image(image, caption='Avg. D 2020_3')
        if options == "Number of devices":
            image = Image.open('./2020_3/# of Devices 2020_3.png')
            st.image(image, caption='# of Devices 2020_3')
        if options == "Avg. Latency (ms)":
            image = Image.open('./2020_3/Avg. Lat Ms 2020_3.png')
            st.image(image, caption='Avg. Lat Ms 2020_3')
    if season == "S4":
        if options == "Avg. Upload Speed":
            image = Image.open('./2020_4/Avg. U 2020_4.png')
            st.image(image, caption='Avg. U 2020_4')
        if options == "Avg. Download Speed":
            image = Image.open('./2020_4/Avg. D 2020_4.png')
            st.image(image, caption='Avg. D 2020_4')
        if options == "Number of devices":
            image = Image.open('./2020_4/# of Devices 2020_4.png')
            st.image(image, caption='# of Devices 2020_4')
        if options == "Avg. Latency (ms)":
            image = Image.open('./2020_4/Avg. Lat Ms 2020_4.png')
            st.image(image, caption='Avg. Lat Ms 2020_4')
