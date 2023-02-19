T = int(input())
for tc in range(1, T+1):
    data = input()
    stack = []
    result = 1
    for s in data:
        if s == '(':
            stack.append(s)
        elif s == '{':
            stack.append(s)

        if s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = 0
                break
        elif s == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                result = 0
                break
    if stack:
        result = 0

    print(f'#{tc} {result}')