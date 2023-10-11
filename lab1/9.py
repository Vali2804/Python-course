def most_common_letter(text):
    letter_counts = {}
    
    
    for char in text:
        if char.isalpha():
            if char not in letter_counts:
                letter_counts[char] = 1
            else:
                letter_counts[char] += 1
    
    most_common = max(letter_counts, key=letter_counts.get)
    
    return most_common, letter_counts[most_common]

text = "an apple is not a tomato"
most_common_letter, count = most_common_letter(text)
print(f"The most common letter is '{most_common_letter}' with a count of {count}.")
