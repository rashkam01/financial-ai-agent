import re


def extract_monetary_values(text):
    """
    Extract monetary values like 21,939 or 23,823 from financial text.
    Returns a list of integers.
    """

    pattern = r"\d{1,3}(?:,\d{3})+"

    matches = re.findall(pattern, text)

    numbers = [int(value.replace(",", "")) for value in matches]

    return numbers