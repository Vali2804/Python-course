def count_words(text):
    words = text.split()
    return len(words)

text = "I have Python exam"
word_cnt = count_words(text)
print(f"The '{text}' has {word_cnt} words")