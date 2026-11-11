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
        "explanation": "Human writers mix short and long sentences. Very even sentence lengths are common in AI text.",
        "evidence": ["variation " + str(stats["variation"]) + " (below 0.35)"],
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
        "explanation": "These ready-made phrases appear far more often in AI text than in human writing.",
        "evidence": found,
    }


def check_transition_openers(text):
    sentences = split_sentences(text)
    found = []
    for sentence in sentences:
        lowered = sentence.lower()
        for word in TRANSITION_WORDS:
            if lowered.startswith(word + ","):
                found.append(word)
    if len(found) < 3:
        return None
    return {
        "name": "Formulaic transitions",
        "explanation": "Starting many sentences with words like 'Moreover,' is a habit of AI text.",
        "evidence": found,
    }


def analyze_ai(text):
    checks = [
        check_uniform_sentences,
        check_stock_phrases,
        check_transition_openers,
    ]
    signals = []
    for check in checks:
        result = check(text)
        if result is not None:
            signals.append(result)
    return signals