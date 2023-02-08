import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list

alpha_dict = {'A' : 14, 'K' : 13, 'Q' : 12, 'J' : 11}
shape_dict = {'clover' : 1, 'heart' : 2, 'diamond' : 3, 'spade' : 4}

trump_card_list = making_card_list()
for time in range(6):
	random.shuffle(trump_card_list)
	# print(trump_card_list[0][0], trump_card_list[0][1])
	player1 = trump_card_list[0]
	player2 = trump_card_list[1]
# 문양을 숫자로 바꾸기
# 숫자부분 AKQJ면 숫자로 바꾸기
# 문양을 먼저 비교하고 
# 같을 때 숫자 부분 비교해야 함
	player1_lst = list(player1)
	player2_lst = list(player2)
	player1_lst[0] = shape_dict[player1[0]] # 이 부분이 문양 바꾸기
	player2_lst[0] = shape_dict[player2[0]] # 이 부분이 문양 바꾸기
	player1_lst[1] = alpha_dict.get(player1[1], player1[1]) # 이 부분이 문양 바꾸기
	player2_lst[1] = alpha_dict.get(player2[1], player2[1]) # 이 부분이 문양 바꾸기
	if player1_lst[0] > player2_lst[0]:
		print(f'{player1} {player2} player1 win!')
	elif player1_lst[0] < player2_lst[0]:
		print(f'{player1} {player2} player2 win!')
	else:
		if player1_lst[1] > player2_lst[1]:
			print(f'{player1} {player2} player1 win!')
		else:
			print(f'{player1} {player2} player2 win!')