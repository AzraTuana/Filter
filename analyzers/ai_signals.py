import re
import statistics

STOCK_PHRASES = [
    "delve into",
    "it's important to note",
    "it is important to note",
    "it is worth noting",
    "in today's fast-paced world",
    "plays a crucial role",
    "navigate the complexities",
    "a testament to",
    "rich tapestry",
    "in conclusion",
    "ever-evolving",
    "unlock the potential",
]

TRANSITION_WORDS = [
    "however",
    "moreover",
    "furthermore",
    "additionally",
    "consequently",
    "overall",
    "ultimately",
    "in addition",
]

CONTRACTION_PATTERN = r"\b(?:\w+n['’]t|\w+['’](?:re|ve|ll|d|m)|(?:it|that|there|what|he|she|let)['’]s)\b"

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
        "explanation": "Human writers mix short and long sentences. Very even sentence lengths are common in AI generated text.",
        "evidence": ["variation " + str(stats["variation"]) + " (below 0.35)"],
        "points": 30,
    }


def check_stock_phrases(text):
    lowered = text.lower()
    found = []
    for phrase in STOCK_PHRASES:
        if phrase in lowered:
            found.append(phrase)
    if len(found) < 2:
        return None
    return {
        "name": "Stock phrases",
        "explanation": "These kind of phrases appear far more often in AI generated text than in human writing.",
        "evidence": found,
        "points": 25,
    }


def check_transition_openers(text):
    sentences = split_sentences(text)
    found = []
    for sentence in sentences:
        lowered = sentence.lower()
        for word in TRANSITION_WORDS:
            if lowered.startswith(word + ","):
                found.append(word + ",")
    if len(found) < 3:
        return None
    return {
        "name": "Formulaic transitions",
        "explanation": "Starting many sentences with words like 'Moreover,' is a habit of AI text.",
        "evidence": found,
        "points": 20,
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


def check_no_contractions(text):
    word_count = len(text.split())
    if word_count < 80:
        return None
    found = re.findall(CONTRACTION_PATTERN, text, flags=re.IGNORECASE)
    if len(found) > 0:
        return None
    return {
        "name": "No contractions",
        "explanation": "People usually write 'don't' or 'it's' at least once in a long text. AI text often avoids them.",
        "evidence": ["0 contractions in " + str(word_count) + " words"],
        "points": 10,
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
        check_stock_phrases,
        check_transition_openers,
        check_lists_of_three,
        check_no_contractions,
    ]
    signals = []
    for check in checks:
        result = check(text)
        if result is not None:
            signals.append(result)
    return signals