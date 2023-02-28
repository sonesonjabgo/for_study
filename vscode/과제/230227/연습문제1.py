data = ''.join(input().split())


for i in range(0, len(data), 7):
    rst = 0
    cnt = 0
    num = data[i:i + 7]
    print(num, end=' ')
    for j in range(-1, -len(num)-1, -1):
        rst += int(num[j]) * (2**cnt)
        cnt += 1
    print(rst)