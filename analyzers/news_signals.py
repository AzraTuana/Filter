import re

CLICKBAIT_PHRASES = [
    "you won't believe",
    "what happened next",
    "shocking",
    "doctors hate",
    "this one trick",
    "they don't want you to know",
    "will blow your mind",
    "goes viral",
    "the truth about",
    "share before it's deleted",
]

VAGUE_SOURCES = [
    "experts say",
    "sources say",
    "studies show",
    "scientists claim",
    "many people are saying",
    "it is said that",
    "according to reports",
    "insiders reveal",
]

EMOTIONAL_WORDS = [
    "outrageous",
    "terrifying",
    "disgusting",
    "horrifying",
    "unbelievable",
    "miracle",
    "disaster",
    "destroyed",
    "evil",
    "scandal",
    "betrayal",
    "nightmare",
]


def get_words(text):
    return re.findall(r"[A-Za-z']+", text)


def find_phrases(text, phrases):
    lowered = text.lower()
    found = []
    for phrase in phrases:
        if phrase in lowered:
            found.append(phrase)
    return found


def check_clickbait(text):
    found = find_phrases(text, CLICKBAIT_PHRASES)
    if len(found) == 0:
        return None
    return {
        "name": "Clickbait phrases",
        "explanation": "These phrases are designed to make you click, not to inform you.",
        "evidence": found,
    }


def check_shouting(text):
    shouted = []
    for word in get_words(text):
        if len(word) >= 4 and word.isupper():
            shouted.append(word)
    if len(shouted) < 3:
        return None
    return {
        "name": "Shouting in capital letters",
        "explanation": "Reliable news rarely writes whole words in capitals. It is a way to trigger emotion.",
        "evidence": shouted[:5],
    }


def check_punctuation(text):
    found = re.findall(r"[!?]{2,}", text)
    exclamations = text.count("!")
    if len(found) == 0 and exclamations < 3:
        return None
    return {
        "name": "Excessive punctuation",
        "explanation": "Repeated exclamation and question marks push excitement instead of facts.",
        "evidence": [str(exclamations) + " exclamation marks"] + found[:3],
    }


def check_vague_sources(text):
    found = find_phrases(text, VAGUE_SOURCES)
    if len(found) == 0:
        return None
    return {
        "name": "Vague sources",
        "explanation": "The text refers to sources without naming them, so the claim cannot be checked.",
        "evidence": found,
    }


def check_emotional_language(text):
    found = find_phrases(text, EMOTIONAL_WORDS)
    if len(found) < 2:
        return None
    return {
        "name": "Emotional language",
        "explanation": "Strongly emotional words try to make you feel something before you think.",
        "evidence": found,
    }


def analyze_news(text):
    checks = [
        check_clickbait,
        check_shouting,
        check_punctuation,
        check_vague_sources,
        check_emotional_language,
    ]
    signals = []
    for check in checks:
        result = check(text)
        if result is not None:
            signals.append(result)
    return signals