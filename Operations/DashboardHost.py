import streamlit as st

st.set_page_config(page_title="", layout="wide")

st.title("📊 Advanced Single Window View - Nestle Payal dashboard ")
st.write("Here's your embedded interactive Prototype report")

powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=13f9b519-b1f3-40ab-895e-5bbca09fc730&autoAuth=true&ctid=21fe27f3-1078-47df-8ff4-55ec1582fd77"

# width must be an int, not a string
st.components.v1.iframe(powerbi_url, height=800, width=1200)
