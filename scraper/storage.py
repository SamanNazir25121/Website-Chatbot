from pathlib import Path


DATA_DIR = Path("data")

DATA_DIR.mkdir(exist_ok=True)


def save_document(filename, text):

    filepath = DATA_DIR / filename

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    print(f"Saved: {filepath}")