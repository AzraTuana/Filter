import streamlit as st

from analyzers.ai_signals import analyze_ai, describe_score, get_score, get_stats
from analyzers.highlight import collect_phrases, highlight_text
from analyzers.news_signals import analyze_news


def show_highlighted_text(text, signals):
    with st.expander("Text with evidence highlighted", expanded=True):
        st.markdown(highlight_text(text, collect_phrases(signals)))


def show_signals(signals):
    for signal in signals:
        st.warning(signal["explanation"], title=signal["name"])
        details = "Evidence: " + " | ".join(signal["evidence"])
        if "points" in signal:
            details += " (+" + str(signal["points"]) + " points)"
        st.caption(details)


st.title("Filter")
st.caption("Paste an article to see suspicious signals and AI-writing traces.")

text = st.text_area("Article text", height=250)

if st.button("Analyze", type="primary"):
    if text.strip() == "":
        st.warning("Please paste some text first.")
    else:
        news_tab, ai_tab = st.tabs(["News signals", "AI-writing signals"])

        with news_tab:
            news_signals = analyze_news(text)
            if len(news_signals) == 0:
                st.success("No suspicious signals found. This does not prove the text is true.")
            else:
                st.markdown(f"Found **{len(news_signals)}** suspicious signals.")
                show_highlighted_text(text, news_signals)
                show_signals(news_signals)

        with ai_tab:
            ai_signals = analyze_ai(text)
            score = get_score(ai_signals)
            stats = get_stats(text)

            with st.container(horizontal=True):
                st.metric("AI-trace score", str(score) + " / 100", border=True)
                st.metric("Sentences", stats["sentences"], border=True)
                st.metric("Average length", stats["average_length"], border=True)
                st.metric("Variation", stats["variation"], border=True)
            st.progress(score / 100, text=describe_score(score))

            if len(ai_signals) == 0:
                st.success("No AI-writing signals found. This does not prove a human wrote it.")
            else:
                show_highlighted_text(text, ai_signals)
                show_signals(ai_signals)
            st.caption(
                "The score adds up the points of the signals found. It is not a probability, "
                "and AI detection is never certain."
            )