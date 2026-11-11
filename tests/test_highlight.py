from analyzers.highlight import collect_phrases, escape_markdown, highlight_text


def test_phrase_is_wrapped():
    result = highlight_text("This is shocking news", ["shocking"])
    assert result == "This is :orange-background[shocking] news"


def test_match_ignores_case_but_keeps_original():
    result = highlight_text("SHOCKING news", ["shocking"])
    assert ":orange-background[SHOCKING]" in result


def test_markdown_characters_are_escaped():
    assert escape_markdown("a*b") == "a\\*b"


def test_collect_phrases_removes_duplicates():
    signals = [{"evidence": ["a", "b"]}, {"evidence": ["b", "c"]}]
    assert collect_phrases(signals) == ["a", "b", "c"]