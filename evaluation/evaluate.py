import os
import random
import urllib.request

import pandas as pd

from analyzers.ai_signals import analyze_ai, get_score

HC3_URL = "https://huggingface.co/datasets/Hello-SimpleAI/HC3/resolve/refs%2Fconvert%2Fparquet/finance/train/0000.parquet"
BENCHMARK_URL = "https://huggingface.co/datasets/textsightai/ai-text-detection-benchmark-2026/resolve/refs%2Fconvert%2Fparquet/"

RESULTS_FILE = "evaluation/results.md"
SAMPLE_SIZE = 1000
THRESHOLDS = [10, 30, 40, 70]


def download(url, file_name):
    path = "data/" + file_name
    if not os.path.exists(path):
        os.makedirs("data", exist_ok=True)
        print("Downloading " + file_name + "...")
        urllib.request.urlretrieve(url, path)
    return path


def load_hc3():
    path = download(HC3_URL, "hc3_finance.parquet")
    table = pd.read_parquet(path)
    human_texts = []
    ai_texts = []
    for index, row in table.iterrows():
        if len(row["human_answers"]) > 0 and len(row["chatgpt_answers"]) > 0:
            human_texts.append(row["human_answers"][0])
            ai_texts.append(row["chatgpt_answers"][0])

    random.seed(42)
    human_texts = random.sample(human_texts, min(SAMPLE_SIZE, len(human_texts)))
    ai_texts = random.sample(ai_texts, min(SAMPLE_SIZE, len(ai_texts)))
    return human_texts, ai_texts


def load_benchmark_part(part_name):
    url = BENCHMARK_URL + part_name + "/train/0000.parquet"
    path = download(url, "benchmark_" + part_name + ".parquet")
    table = pd.read_parquet(path)
    return list(table["text"])


def load_benchmark():
    human_texts = load_benchmark_part("human_wikipedia_pre2022")
    human_texts += load_benchmark_part("human_pmc_ccby_nonanglophone")
    ai_texts = load_benchmark_part("ai_generated_2026")
    return human_texts, ai_texts


def analyze_group(texts):
    scores = []
    signal_counts = {}
    for text in texts:
        signals = analyze_ai(text)
        scores.append(get_score(signals))
        for signal in signals:
            name = signal["name"]
            signal_counts[name] = signal_counts.get(name, 0) + 1
    return scores, signal_counts


def percent(part, whole):
    return round(100 * part / whole, 1)


def count_flagged(scores, threshold):
    flagged = 0
    for score in scores:
        if score >= threshold:
            flagged += 1
    return flagged


def build_report(title, human_texts, ai_texts):
    human_scores, human_counts = analyze_group(human_texts)
    ai_scores, ai_counts = analyze_group(ai_texts)

    lines = []
    lines.append("## " + title)
    lines.append("")
    lines.append(str(len(human_scores)) + " human texts and " + str(len(ai_scores)) + " AI texts.")
    lines.append("")
    lines.append("### How often each signal fires")
    lines.append("")
    lines.append("| Signal | Human texts | AI texts |")
    lines.append("|---|---|---|")
    names = sorted(set(human_counts) | set(ai_counts))
    for name in names:
        human_rate = percent(human_counts.get(name, 0), len(human_scores))
        ai_rate = percent(ai_counts.get(name, 0), len(ai_scores))
        lines.append("| " + name + " | " + str(human_rate) + "% | " + str(ai_rate) + "% |")
    lines.append("")
    lines.append("### Results at different score thresholds")
    lines.append("")
    lines.append("| Flag if score is at least | AI texts caught | Human texts wrongly flagged | Balanced accuracy |")
    lines.append("|---|---|---|---|")
    for threshold in THRESHOLDS:
        caught = percent(count_flagged(ai_scores, threshold), len(ai_scores))
        false_alarms = percent(count_flagged(human_scores, threshold), len(human_scores))
        balanced = round((caught + (100 - false_alarms)) / 2, 1)
        lines.append("| " + str(threshold) + " | " + str(caught) + "% | "
                     + str(false_alarms) + "% | " + str(balanced) + "% |")
    lines.append("")
    return "\n".join(lines)


def main():
    report = "# Evaluation results\n\n"

    human_texts, ai_texts = load_hc3()
    report += build_report("HC3 finance (ChatGPT, early 2023)", human_texts, ai_texts)
    report += "\n"

    human_texts, ai_texts = load_benchmark()
    report += build_report("TextSight benchmark (five models, September 2026)", human_texts, ai_texts)

    print(report)
    with open(RESULTS_FILE, "w", encoding="utf-8") as file:
        file.write(report)
    print("Saved to " + RESULTS_FILE)


if __name__ == "__main__":
    main()