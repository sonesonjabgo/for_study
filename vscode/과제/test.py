# print(list(range(10, 0, -1)))

# name = [1, 2, 3, 4]
# # print(name[:3])
# mlist = [0, 0, 0]
# mlist[0] += 1
# print(mlist)
# arr = [[0 for _ in range(10)] for _ in range(10)]
# print(arr)

# my_list = [0,0,0,0,0,0,0]
# # my_list[:4] = 1
my_list = [5, 8, 3]
i = 0
while True:
    my_list[i] = my_list[i] // 2
    if my_list[i] == 0:
        my_list[i] = 1
    i = (i+1) % len(my_list) # N
