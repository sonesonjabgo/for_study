T = int(input())

for i in range(T):
    stack = []
    laser = 0
    stick = 0
    a=input()
    for k in a:
        if k == '(':
            stack.append(k)
            for j in a:
                if j == '(':
                    stack.append(j)
                else:
                    laser += 1
                    stack.pop()
        elif k == ')':
            if stack:
                stack.pop()
                stick += 1
    print(stick + laser)