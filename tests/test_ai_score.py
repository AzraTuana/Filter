from analyzers.ai_signals import (
    analyze_ai,
    check_lists_of_three,
    check_no_contractions,
    describe_score,
    get_score,
)

LONG_FORMAL_TEXT = "The committee has reviewed the proposal in detail. " * 12


def test_two_lists_of_three_are_flagged():
    text = "We need clear goals, strong teams, and steady growth. It is fast, simple, and reliable."
    assert check_lists_of_three(text) is not None


def test_one_list_of_three_is_not_enough():
    assert check_lists_of_three("I bought apples, pears, and plums.") is None


def test_long_text_without_contractions_is_flagged():
    assert check_no_contractions(LONG_FORMAL_TEXT) is not None


def test_text_with_a_contraction_is_not_flagged():
    assert check_no_contractions(LONG_FORMAL_TEXT + " We don't agree.") is None


def test_short_text_is_not_checked_for_contractions():
    assert check_no_contractions("This is short.") is None


def test_score_adds_points():
    assert get_score([{"points": 30}, {"points": 25}]) == 55


def test_score_never_goes_above_100():
    text = "In today's fast-paced world, data plays a crucial role in modern life. " * 3
    assert get_score(analyze_ai(text)) <= 100


def test_describe_score():
    assert describe_score(0) == "Few AI traces found"
    assert describe_score(30) == "Some AI traces found"
    assert describe_score(80) == "Many AI traces found"