from analyzers.ai_signals import check_stock_phrases, check_uniform_sentences, split_sentences


def test_split_sentences():
    assert split_sentences("One. Two! Three?") == ["One.", "Two!", "Three?"]


def test_uniform_sentences_are_flagged():
    text = "The cat sat on the mat. The dog ran in the park. The bird flew to the tree. The fish swam in the pond. The cow stood in the field."
    assert check_uniform_sentences(text) is not None


def test_varied_sentences_are_not_flagged():
    text = "No. I walked all the way to the old harbour before the rain finally started. It poured. We ran. Nobody had thought to bring an umbrella, which was typical of us."
    assert check_uniform_sentences(text) is None


def test_one_stock_phrase_is_not_enough():
    assert check_stock_phrases("Let us delve into the topic.") is None