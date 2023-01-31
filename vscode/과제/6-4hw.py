# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 


def anagram(words):
    sorted_words = map(sorted,words) # sorted 적용된 리스트 만들어짐
    wordsets = set(map(tuple,sorted_words))
    # # 중복 제거를 위해 set에 넣어줌
    # # 리스트를 그대로 set에 넣어줄 수 없기 때문에
    # # map을 활용해 tuple로 만들어준다.
    words_dict = {key : [] for key in wordsets}
    # # 이제 빈 리스트에 word를 넣어줘야 함
    for word in words:
        sorted_word = tuple(sorted(word)) # ['a','t','e'] > ('a','t','e')
        words_dict[sorted_word].append(word)

    vl = list(words_dict.values()) 
    print(vl)

anagram(['eat','tea','tan','ate','nat','bat'])