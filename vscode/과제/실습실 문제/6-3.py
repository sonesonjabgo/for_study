def count_vowels(word):
    vowel = ['a','e','i','o','u']
    vowel_count = 0
    for str in word:
        if str in vowel:
            vowel_count += 1
    
    print(vowel_count)
    return vowel_count









count_vowels('apple') #=> 2
count_vowels('banana') #=> 3