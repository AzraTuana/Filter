from analyzers.news_signals import analyze_news, check_clickbait, check_shouting


def test_clickbait_is_found():
    result = check_clickbait("You won't believe this story")
    assert result is not None
    assert "you won't believe" in result["evidence"]


def test_one_capital_word_is_not_shouting():
    assert check_shouting("NASA launched a rocket today") is None


def test_clean_text_has_no_signals():
    text = "The council voted on Tuesday to approve the budget."
    assert analyze_news(text) == []