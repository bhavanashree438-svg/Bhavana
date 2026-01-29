import streamlit as st

st.set_page_config(page_title="Cartoon Names App", layout="centered")

st.title("🎨 Popular Cartoon Names")

st.write("Below are some popular cartoon characters:")

cartoon_names = [
    "Doraemon",
    "Tom and Jerry",
    "Mickey Mouse",
    "Shinchan",
    "Pikachu",
    "Scooby-Doo",
    "Bugs Bunny"
]

for cartoon in cartoon_names:
    st.markdown(f"- **{cartoon}**")

st.success("Cartoon list displayed successfully!")
