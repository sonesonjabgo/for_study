operator = ['+', '-', '*', '/', '.']

T = int(input())
for tc in range(1, T+1):
    data = input().split()
    op = []
    num = []
    for i in data:
        if i not in operator:
            num.append(i)
        else:
            try:
                op.append(i)
                if op[-1] == operator[0]:
                    op2 = int(num.pop())
                    op1 = int(num.pop())
                    number = op1 + op2
                    num.append(number)
                elif op[-1] == operator[1]:
                    op2 = int(num.pop())
                    op1 = int(num.pop())
                    number = op1 - op2
                    num.append(number)
                elif op[-1] == operator[2]:
                    op2 = int(num.pop())
                    op1 = int(num.pop())
                    number = op1 * op2
                    num.append(number)
                elif op[-1] == operator[3]:
                    op2 = int(num.pop())
                    op1 = int(num.pop())
                    number = op1 // op2
                    num.append(number)
                else:
                    if len(num) == 1:
                        print(f'#{tc} {num[-1]}')
                    else:
                        print(f'#{tc} error')
                op.pop()
            except IndexError:
                print(f'#{tc} error')
                break


