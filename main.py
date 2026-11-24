"""One-Line Office Joke: 24-Hour Sprint.

Writes a single one-line joke about office life to entry.txt.
The joke is one sentence, one line, under 200 characters.
"""

import os

JOKE = "The office printer only jams on documents marked urgent, which is how I know it can read."


def main():
    # Gate check, mirroring the competition scorer: 1-200 chars, one line.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)


if __name__ == "__main__":
    main()
