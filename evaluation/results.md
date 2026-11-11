# Evaluation results

## HC3 finance (ChatGPT, early 2023)

1000 human texts and 1000 AI texts.

### How often each signal fires

| Signal | Human texts | AI texts |
|---|---|---|
| Comma-heavy sentences | 2.6% | 23.8% |
| Filler words | 8.7% | 71.8% |
| Lists of three | 3.4% | 14.6% |
| No short sentences | 5.6% | 67.2% |
| Uniform sentence length | 7.2% | 16.4% |

### Results at different score thresholds

| Flag if score is at least | AI texts caught | Human texts wrongly flagged | Balanced accuracy |
|---|---|---|---|
| 15 | 89.6% | 23.0% | 83.3% |
| 30 | 66.3% | 8.3% | 79.0% |
| 40 | 61.7% | 3.3% | 79.2% |
| 55 | 31.5% | 2.2% | 64.7% |
| 70 | 16.0% | 0.6% | 57.7% |

## TextSight benchmark (five models, September 2026)

338 human texts and 56 AI texts.

### How often each signal fires

| Signal | Human texts | AI texts |
|---|---|---|
| Comma-heavy sentences | 26.9% | 57.1% |
| Filler words | 7.7% | 14.3% |
| Lists of three | 15.1% | 44.6% |
| No short sentences | 30.8% | 80.4% |
| Uniform sentence length | 15.1% | 75.0% |

### Results at different score thresholds

| Flag if score is at least | AI texts caught | Human texts wrongly flagged | Balanced accuracy |
|---|---|---|---|
| 15 | 91.1% | 57.4% | 66.8% |
| 30 | 83.9% | 30.8% | 76.6% |
| 40 | 78.6% | 22.2% | 78.2% |
| 55 | 73.2% | 13.9% | 79.7% |
| 70 | 51.8% | 5.3% | 73.2% |
