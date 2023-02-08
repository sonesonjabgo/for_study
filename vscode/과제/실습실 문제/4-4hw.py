words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

sorted_words = map(sorted, words)
word_set = set(map(tuple, sorted_words))
word_dict = {key : [] for key in word_set}

for word in words:
    sorted_word = tuple(sorted(word))
    word_dict[sorted_word].append(word)

print(list(word_dict.values()))