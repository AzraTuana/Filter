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

## Multi-domain test set (11 kinds of text, many models)

9998 human texts and 4947 AI texts.

### How often each signal fires

| Signal | Human texts | AI texts |
|---|---|---|
| Comma-heavy sentences | 7.8% | 5.7% |
| Filler words | 4.2% | 16.3% |
| Lists of three | 15.4% | 17.5% |
| No short sentences | 6.3% | 21.5% |
| Uniform sentence length | 9.3% | 32.7% |

### Results at different score thresholds

| Flag if score is at least | AI texts caught | Human texts wrongly flagged | Balanced accuracy |
|---|---|---|---|
| 15 | 55.0% | 33.6% | 60.7% |
| 30 | 37.9% | 13.1% | 62.4% |
| 40 | 25.0% | 5.3% | 59.9% |
| 55 | 17.0% | 3.0% | 57.0% |
| 70 | 6.2% | 0.7% | 52.8% |

### Results by kind of text (score 40 or more counts as flagged)

| Kind of text | Human texts | AI texts | AI texts caught | Human texts wrongly flagged | Balanced accuracy |
|---|---|---|---|---|---|
| academic_abstract | 2154 | 817 | 50.1% | 13.0% | 68.5% |
| encyclopedic_reference | 2132 | 601 | 32.4% | 3.8% | 64.3% |
| essay | 227 | 227 | 48.5% | 9.7% | 69.4% |
| forum_qa | 2149 | 919 | 22.1% | 0.9% | 60.6% |
| howto_instructional | 236 | 70 | 11.4% | 5.1% | 53.2% |
| news | 234 | 73 | 21.9% | 7.7% | 57.1% |
| review_opinion | 294 | 123 | 17.1% | 2.4% | 57.3% |
| web_text | 2049 | 1977 | 12.4% | 3.5% | 54.5% |

### AI texts caught, by the model that wrote them (score 40 or more)

| Model | Texts | Caught |
|---|---|---|
| ateeqq:unknown_model | 104 | 55.8% |
| bloomz | 110 | 20.0% |
| chatgpt | 590 | 27.5% |
| claude-haiku-4.5 | 53 | 41.5% |
| cohere | 152 | 36.8% |
| cohere-chat | 55 | 34.5% |
| davinci | 98 | 31.6% |
| dolly | 73 | 27.4% |
| gemini-2.5-flash | 81 | 18.5% |
| gemma-7b-it | 70 | 44.3% |
| gemma2-9b-it | 61 | 37.7% |
| gpt-3.5-turbo | 243 | 49.0% |
| gpt-35 | 178 | 46.1% |
| gpt-4.1-2025-04-14 | 57 | 19.3% |
| gpt-5-nano | 60 | 30.0% |
| gpt2 | 58 | 25.9% |
| gpt2_xl | 438 | 3.0% |
| gpt3 | 53 | 9.4% |
| gpt4 | 91 | 44.0% |
| gpt4o | 83 | 53.0% |
| llama | 454 | 6.8% |
| llama-chat | 55 | 56.4% |
| llama3-70b | 62 | 53.2% |
| llama3-8b | 73 | 53.4% |
| mixtral-8x7b | 94 | 45.7% |
| mpt | 56 | 21.4% |
| palm | 424 | 10.4% |
| text-davinci-003 | 75 | 26.7% |
