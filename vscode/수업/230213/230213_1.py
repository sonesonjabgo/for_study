# stack 연습문제 1
stack = [0]*3
top = -1

top += 1 # push(10)
stack[top] = 10

top += 1 # push(20)
stack[top] = 20

top += 1 # push(30)
stack[top] = 30

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])

top -= 1
print(stack[top+1])