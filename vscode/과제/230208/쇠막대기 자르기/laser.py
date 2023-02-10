T = int(input())

for i in range(T):
    stack = []
    laser = 0
    stick = 0
    a=input()
    for k in a:
        if k == '(':
            stack.append(k)
            for j in range(len(a)):
                if a[j] == '(':
                    if a[j+1] == ')':
                        laser += 1
                    else:
                        break
                else:
                    break
        elif k == ')':
            if stack:
                stack.pop()
                stick += 1
    print(stick + laser)