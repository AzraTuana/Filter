# Filter

A small tool that highlights suspicious signals and AI-writing traces in news text, comments and articles.

**[Try the demo](https://filter-me.streamlit.app/)**

## Why

Misleading articles and AI written comments are everywhere, and most of us share 
or believe things without reading them closely. Filter does not tell you what is true. It
points at the parts of a text that deserve a second look, and explains why.

## What it checks

### News signals

| Signal | What it looks for |
|---|---|
| Clickbait phrases | "you won't believe", "what happened next" |
| Shouting | Several words written entirely in capitals |
| Excessive punctuation | "!!!", "?!", many exclamation marks |
| Vague sources | "experts say", "studies show" with no name attached |
| Emotional language | Words chosen to provoke rather than inform |

### AI-writing signals

| Signal | What it looks for |
|---|---|
| Uniform sentence length | Sentences that are all nearly the same length |
| Stock phrases | "delve into", "plays a crucial role" |
| Formulaic transitions | Sentences opening with "Moreover,", "Furthermore," |

## How it works

Every check is a small Python function that returns either nothing or a signal
with a name, an explanation and the evidence found in the text. There is no
machine learning model: every result can be traced back to a rule you can read
in `analyzers/`.

Sentence uniformity uses the coefficient of variation (standard deviation of
sentence lengths divided by their mean). Values below 0.35 are flagged.

## Limitations

- **This is not a fact checker.** A text with no signals can still be false, and
  a true story can be written in a sensational style.
- **AI detection is never certain.** A formal human writer can trigger every
  AI signal, and a model asked to write casually can trigger none.
- Sentence splitting is naive and treats abbreviations like "Dr." as sentence ends.
- The phrase lists are short, hand-picked and English only.

## Run it locally

```bash
git clone https://github.com/AzraTuana/Filter.git
cd Filter
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m streamlit run app.py
```

On macOS and Linux use `.venv/bin/python` instead of `.venv\Scripts\python`.

## Run the tests

```bash
.venv\Scripts\python -m pip install -r requirements-dev.txt
.venv\Scripts\python -m pytest
```

## Roadmap

- [ ] Missing attribution check
- [ ] Claim extraction with a language model
- [ ] Highlight the evidence inside the original text

## Built with

Python, Streamlit, pytest.