import re
from collections import Counter
from pathlib import Path


def analyze_text(text):
    words = re.findall(r"\b\w+\b", text.lower())

    characters = len(text)
    word_count = len(words)

    sentences = len(
        re.findall(r"[.!?]+", text)
    )

    frequency = Counter(words)

    print("\n===== TEXT ANALYSIS =====")
    print(f"Total Characters: {characters}")
    print(f"Total Words: {word_count}")
    print(f"Sentence Endings: {sentences}")

    print("\nTop 5 Most Common Words:")

    for word, count in frequency.most_common(5):
        print(f"{word}: {count}")


def main():
    filename = input("Enter text file path: ")

    file_path = Path(filename)

    try:
        text = file_path.read_text(encoding="utf-8")
        analyze_text(text)

    except FileNotFoundError:
        print("File not found!")

    except (OSError, UnicodeError) as e:
        print(f"Unable to read file: {e}")


if __name__ == "__main__":
    main()