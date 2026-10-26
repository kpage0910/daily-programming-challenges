from collections import Counter

def first_unique_word(sentence: str) -> str | None:

    sentence = sentence.replace(",","").replace(".", "").replace("!", "").replace("?", "")
    sentence = sentence.lower().split()
    word_counts = Counter(sentence)

    for word in sentence:
        if word_counts[word] == 1:
            return word
        

print(first_unique_word("Hello, hello! World?"))