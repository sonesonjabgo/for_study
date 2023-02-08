# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
 

# word = input()
# lastfirst = word[-1]
# # lastfirst로 다음 input 단어가 시작해야 함
# # words 리스트에 word를 저장
# # words 리스트에 새 input 단어가 존재하면 done
# # input이 한번 진행되면 숫자가 1씩 늘어나야 함

# words = []
# words.append(word)

# # words[0] > words[1] > ''' > words[n] > done
# # words[n][-1] == words[n+1][0]이지 않으면 done
# # 첫 단어는 전 단어가 없다
# # n == 0 이면 pass

# word = input()
# words = []
# words.append(word)
# # 위에 얘네도 반복되어야 함

words = []
n = 0
while True:
    word = input('단어를 입력하시오 : ')
    words.append(word)
    
    lastfirst = words[n-1][-1] # 전 단어 마지막 글자
    firstlast = words[n][0]    # 현재 단어 첫 글자
    for i in words:   # 단어 중복 시 끝내기
        if i == word:
            break
    if n == 0: # 첫 단어 제외
        pass
    else:
        if lastfirst == firstlast:
            pass
        else:
            break
    n += 1

print('땡!')
print(f'{n+1}번 째에서 끝났습니다.')
# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
# 이전에 쓴 단어 못 쓰게 해야 함
# done 입력할 때 끝나야 함
