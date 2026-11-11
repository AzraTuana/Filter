import re
import string


def escape_markdown(text):
    escaped = ""
    for char in text:
        if char in string.punctuation:
            escaped += "\\" + char
        else:
            escaped += char
    return escaped


def collect_phrases(signals):
    phrases = []
    for signal in signals:
        for item in signal["evidence"]:
            if item not in phrases:
                phrases.append(item)
    return phrases


def highlight_text(text, phrases, color="orange"):
    if len(phrases) == 0:
        return escape_markdown(text).replace("\n", "  \n")

    longest_first = sorted(phrases, key=len, reverse=True)
    escaped_phrases = []
    for phrase in longest_first:
        escaped_phrases.append(re.escape(phrase))
    pattern = "(" + "|".join(escaped_phrases) + ")"

    parts = re.split(pattern, text, flags=re.IGNORECASE)
    result = ""
    for index, part in enumerate(parts):
        if index % 2 == 1:
            result += ":" + color + "-background[" + escape_markdown(part) + "]"
        else:
            result += escape_markdown(part)
    return result.replace("\n", "  \n")