import streamlit as st

st.title("Filter")
st.write("Paste a news article to see suspicious signals and AI-writing traces.")

text = st.text_area("Article text", height=250)

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please paste some text first.")
    else:
        words = text.split()
        st.write("Words:", len(words))