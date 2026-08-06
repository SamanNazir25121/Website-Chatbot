import re


REMOVE_PATTERNS = [
    "Support Us",
    "Read More",
    "×",
    "Follow Us",
    "Submit",
    "Contact Us",
    "Home",
    "About Us",
    "Take a look at our projects",
    "Technical Areas - Lums Energy Institute"
]

def remove_duplicates(lines):

    seen = set()
    cleaned = []

    for line in lines:

        normalized = line.lower().strip()

        if normalized not in seen:

            cleaned.append(line)
            seen.add(normalized)

    return cleaned

def clean_text(text):

    text = re.sub(
        r'[ \t]+',
        ' ',
        text
    )


    lines = []

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue


        if line in REMOVE_PATTERNS:
            continue


        lines.append(line)


    # remove duplicate lines
    lines = remove_duplicates(lines)


    return "\n".join(lines)