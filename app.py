import streamlit as st

from analyzers.news_signals import analyze_news

st.title("Filter")
st.caption("Paste a news article to see suspicious signals and AI-writing traces.")

text = st.text_area("Article text", height=250)

if st.button("Analyze", type="primary"):
    if text.strip() == "":
        st.warning("Please paste some text first.")
    else:
        signals = analyze_news(text)

        st.subheader("News signals")
        if len(signals) == 0:
            st.success("No suspicious signals found. This does not prove the text is true.")
        else:
            st.markdown(f"Found **{len(signals)}** suspicious signals.")
            for signal in signals:
                st.warning(signal["explanation"], title=signal["name"])
                st.caption("Evidence: " + ", ".join(signal["evidence"]))