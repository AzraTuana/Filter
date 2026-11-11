import re
import statistics

FILLER_WORDS = [
    "may",
    "can",
    "often",
    "typically",
    "various",
    "several",
    "such",
    "including",
    "while",
    "both",
    "range",
    "significant",
    "key",
    "crucial",
    "essential",
    "important",
    "overall",
    "particularly",
]

LIST_OF_THREE_PATTERN = r"[^,.;:!?\n]{1,40}, [^,.;:!?\n]{1,40}, and \w+"


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    sentences = []
    for part in parts:
        if part.strip() != "":
            sentences.append(part.strip())
    return sentences


def sentence_lengths(text):
    lengths = []
    for sentence in split_sentences(text):
        lengths.append(len(sentence.split()))
    return lengths


def get_words(text):
    return re.findall(r"[A-Za-z']+", text)


def get_stats(text):
    lengths = sentence_lengths(text)
    if len(lengths) < 2:
        return {"sentences": len(lengths), "average_length": 0.0, "variation": 0.0}
    average = statistics.mean(lengths)
    variation = statistics.stdev(lengths) / average
    return {
        "sentences": len(lengths),
        "average_length": round(average, 1),
        "variation": round(variation, 2),
    }


def check_uniform_sentences(text):
    stats = get_stats(text)
    if stats["sentences"] < 5:
        return None
    if stats["variation"] >= 0.35:
        return None
    return {
        "name": "Uniform sentence length",
        "explanation": "Human writers mix short and long sentences. Very even sentence lengths are common in AI text.",
        "evidence": ["variation " + str(stats["variation"]) + " (below 0.35)"],
        "points": 30,
    }


def check_no_short_sentences(text):
    lengths = sentence_lengths(text)
    if len(lengths) < 4:
        return None
    shortest = min(lengths)
    if shortest < 14:
        return None
    return {
        "name": "No short sentences",
        "explanation": "People drop in a short sentence now and then. Here even the shortest sentence is long, which is common in AI text.",
        "evidence": ["shortest sentence has " + str(shortest) + " words (14 or more)"],
        "points": 25,
    }


def check_lists_of_three(text):
    found = []
    for match in re.findall(LIST_OF_THREE_PATTERN, text):
        found.append(match.strip())
    if len(found) < 2:
        return None
    return {
        "name": "Lists of three",
        "explanation": "AI text loves grouping things in threes, like 'clear, simple, and effective'.",
        "evidence": found,
        "points": 15,
    }


def check_comma_heavy(text):
    sentence_count = len(split_sentences(text))
    if sentence_count < 4:
        return None
    commas_per_sentence = round(text.count(",") / sentence_count, 1)
    if commas_per_sentence < 2.0:
        return None
    return {
        "name": "Comma-heavy sentences",
        "explanation": "AI text tends to pack several clauses into every sentence, so it uses many commas.",
        "evidence": [str(commas_per_sentence) + " commas per sentence (2.0 or more)"],
        "points": 15,
    }


def check_filler_words(text):
    words = get_words(text)
    if len(words) < 80:
        return None
    count = 0
    for word in words:
        if word.lower() in FILLER_WORDS:
            count += 1
    share = round(100 * count / len(words), 1)
    if share < 2.5:
        return None
    return {
        "name": "Filler words",
        "explanation": "Words like 'various', 'crucial' and 'typically' add little meaning. Older AI models use them a lot; newer ones much less.",
        "evidence": [str(share) + "% of the words are filler words (2.5% or more)"],
        "points": 15,
    }


def get_score(signals):
    score = 0
    for signal in signals:
        score += signal["points"]
    return score


def describe_score(score):
    if score >= 60:
        return "Many AI traces found"
    if score >= 25:
        return "Some AI traces found"
    return "Few AI traces found"


def analyze_ai(text):
    checks = [
        check_uniform_sentences,
        check_no_short_sentences,
        check_lists_of_three,
        check_comma_heavy,
        check_filler_words,
    ]
    signals = []
    for check in checks:
        result = check(text)
        if result is not None:
            signals.append(result)
    return signals