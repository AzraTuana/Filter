import streamlit as st

from analyzers.ai_signals import analyze_ai, get_stats
from analyzers.news_signals import analyze_news


def show_signals(signals, empty_message):
    if len(signals) == 0:
        st.success(empty_message)
        return
    st.markdown(f"Found **{len(signals)}** suspicious signals.")
    for signal in signals:
        st.warning(signal["explanation"], title=signal["name"])
        st.caption("Evidence: " + ", ".join(signal["evidence"]))


st.title("Filter")
st.caption("Paste a news article to see suspicious signals and AI-writing traces.")

text = st.text_area("Article text", height=250)

if st.button("Analyze", type="primary"):
    if text.strip() == "":
        st.warning("Please paste some text first.")
    else:
        news_tab, ai_tab = st.tabs(["News signals", "AI-writing signals"])

        with news_tab:
            show_signals(
                analyze_news(text),
                "No suspicious signals found. This does not prove the text is true.",
            )

        with ai_tab:
            stats = get_stats(text)
            with st.container(horizontal=True):
                st.metric("Sentences", stats["sentences"], border=True)
                st.metric("Average length", stats["average_length"], border=True)
                st.metric("Variation", stats["variation"], border=True)
            show_signals(
                analyze_ai(text),
                "No AI-writing signals found. This does not prove a human wrote it.",
            )
            st.caption("These signals are hints, not proof. AI detection is never certain.")