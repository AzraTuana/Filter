from analyzers.ai_signals import (
    check_comma_heavy,
    check_filler_words,
    check_no_short_sentences,
    check_uniform_sentences,
    split_sentences,
)

LONG_SENTENCE = "The committee reviewed the proposal in great detail before it reached a final decision on the matter."


def test_split_sentences():
    assert split_sentences("One. Two! Three?") == ["One.", "Two!", "Three?"]


def test_uniform_sentences_are_flagged():
    text = "The cat sat on the mat. The dog ran in the park. The bird flew to the tree. The fish swam in the pond. The cow stood in the field."
    assert check_uniform_sentences(text) is not None


def test_varied_sentences_are_not_flagged():
    text = "No. I walked all the way to the old harbour before the rain finally started. It poured. We ran. Nobody had thought to bring an umbrella, which was typical of us."
    assert check_uniform_sentences(text) is None


def test_only_long_sentences_are_flagged():
    text = " ".join([LONG_SENTENCE] * 4)
    assert check_no_short_sentences(text) is not None


def test_one_short_sentence_is_enough_to_pass():
    text = " ".join([LONG_SENTENCE] * 4) + " It passed."
    assert check_no_short_sentences(text) is None


def test_too_few_sentences_are_not_checked():
    assert check_no_short_sentences(LONG_SENTENCE) is None


def test_many_commas_are_flagged():
    sentence = "The plan, which was new, bold, and risky, passed."
    text = " ".join([sentence] * 4)
    assert check_comma_heavy(text) is not None


def test_few_commas_are_not_flagged():
    text = "We met on Monday. The plan passed. Nobody objected, which was a surprise. Then we left."
    assert check_comma_heavy(text) is None


def test_many_filler_words_are_flagged():
    text = "It is important to use various key tools because they can often help. " * 8
    assert check_filler_words(text) is not None


def test_plain_text_has_no_filler_signal():
    text = "The train left the station at nine and reached the coast before noon. " * 8
    assert check_filler_words(text) is None

def test_headings_and_list_markers_are_not_sentences():
    text = "1. A Heading Here\nFirst sentence here. Second one!\n- Option A: a list item."
    assert split_sentences(text) == ["First sentence here.", "Second one!", "Option A: a list item."]


def test_long_line_without_final_period_is_kept():
    text = "This is a long line that someone pasted without the final period at the very end of it"
    assert len(split_sentences(text)) == 1