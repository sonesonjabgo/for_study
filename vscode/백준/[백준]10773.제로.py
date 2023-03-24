K = int(input())
data = [int(input()) for _ in range(K)]
stack = []
for i in data:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))