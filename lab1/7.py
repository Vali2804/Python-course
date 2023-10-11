import re

def extract_number(text):
    pattern = r'\d+'
    match = re.search(pattern, text)
    if match:
        extracted_number = int(match.group())
        return extracted_number
    else:
        return None

text1 = "An apple is 123 USD"
result1 = extract_number(text1)
print(f"Extracted number from '{text1}': {result1}")

text2 = "abc123abc"
result2 = extract_number(text2)
print(f"Extracted number from '{text2}': {result2}")
