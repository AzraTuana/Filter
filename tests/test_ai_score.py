from analyzers.ai_signals import (
    analyze_ai,
    check_lists_of_three,
    describe_score,
    get_score,
)


def test_two_lists_of_three_are_flagged():
    text = "We need clear goals, strong teams, and steady growth. It is fast, simple, and reliable."
    assert check_lists_of_three(text) is not None


def test_one_list_of_three_is_not_enough():
    assert check_lists_of_three("I bought apples, pears, and plums.") is None


def test_score_adds_points():
    assert get_score([{"points": 30}, {"points": 25}]) == 55


def test_score_never_goes_above_100():
    text = "It is important to use various key tools, clear plans, and steady teams, because they can often help in several ways. " * 8
    assert get_score(analyze_ai(text)) == 100


def test_describe_score():
    assert describe_score(0) == "Few AI traces found"
    assert describe_score(30) == "Some AI traces found"
    assert describe_score(80) == "Many AI traces found"