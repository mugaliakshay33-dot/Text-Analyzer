# Python Text Analyzer

A simple Python tool that analyzes text files and displays character counts, word counts, sentence-ending punctuation counts, and the five most frequently used words.

## Features

* Counts total characters and words.
* Counts sentence-ending punctuation.
* Identifies the top 5 most common words.
* Supports UTF-8 text files.
* Handles file errors.

## Technologies Used

* Python 3
* Regular Expressions (`re`)
* Collections (`Counter`)
* File Handling (`pathlib`)

## How to Run

1. Download `text_analyzer.py`.
2. Open the project in VS Code.
3. Run the command:

```bash
python text_analyzer.py
```

4. Enter your text file path.
5. View the analysis results.

## Example Output

```text
===== TEXT ANALYSIS =====
Total Characters: 32
Total Words: 6
Sentence Endings: 2

Top 5 Most Common Words:
python: 2
is: 2
fun: 1
useful: 1
```

## Project Structure

```text
Python-Text-Analyzer/
│
├── text_analyzer.py
└── README.md
```

## Learning Outcomes

This project demonstrates Python programming concepts such as file handling, regular expressions, text processing, and word frequency analysis.
