# Evaluation results

## HC3 finance (ChatGPT, early 2023)

1000 human texts and 1000 AI texts.

### How often each signal fires

| Signal | Human texts | AI texts |
|---|---|---|
| Formulaic transitions | 0.1% | 0.2%  |
| Lists of three | 3.4% | 14.6% |
| No contractions | 21.4% | 52.0% |
| Uniform sentence length | 7.2% | 16.4% |

### Results at different score thresholds

| Flag if score is at least | AI texts caught | Human texts wrongly flagged | Balanced accuracy |
|---|---|---|---|
| 10 | 66.4% | 29.6% | 68.4% |
| 25 | 22.3% | 7.6% | 57.4% |
| 40 | 9.5% | 2.1% | 53.7% |
| 60 | 0.0% | 0.0% | 50.0% |

## TextSight benchmark (five models, September 2026)

338 human texts and 56 AI texts.

### How often each signal fires

| Signal | Human texts | AI texts |
|---|---|---|
| Lists of three | 15.1% | 44.6% |
| No contractions | 100.0% | 100.0% |
| Uniform sentence length | 15.1% | 75.0% |

### Results at different score thresholds

| Flag if score is at least | AI texts caught | Human texts wrongly flagged | Balanced accuracy |
|---|---|---|---|
| 10 | 100.0% | 100.0% | 50.0% |
| 25 | 78.6% | 27.2% | 75.7% |
| 40 | 75.0% | 15.1% | 80.0% |
| 60 | 0.0% | 0.0% | 50.0% |
