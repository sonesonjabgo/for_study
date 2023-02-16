# 후위표기식 스택 활용 알고리즘
# 2 + 3 * 4 / 5
isp = {'*':2 , '/':2, '+':1, '-':1, '(': 0}
icp = {'*':2 , '/':2, '+':1, '-':1, '(': 3}

data = input()
# '2+3*4/5'

# 피연산자는 그냥 출력
# 연산자는 우선순위에 따라서 stack 넣거나, 빼고 넣기
# stack의 top의 우선순위보다 token의 우선순위가 높으면 그냥 stack에 넣어주기
# 아니면 높거나 같은애들은 다 빼고 낮은애가 나오면 push
# 닫히는 괄호 나오면 여는 괄호 나올 때까지 pop하면서 출력하기

stack = []
for i in range(len(data)):
    # 피연산자인지 연산자인지 확인
    if data[i] in '0123456789': # 피연산자임
        print(data[i], end='')
    else: # 연산자임
        if data[i] == ')':
            # 여는 괄호가 나올때 까지 pop하면서 연산자 출력
            while stack[-1] != '(':
                print(stack.pop(), end='')
            # 여는 괄호 버리기
            stack.pop()
        elif not stack: # 스택이 비어있으면
            stack.append(data[i])
        else: # 스택이 비어있지 않으면 우선순위를 따져야 함
            if isp[stack[-1]] < icp[data[i]]: # data[i]가 우선순위 높으면
                stack.append(data[i]) # push
            else: # 우선순위가 같거나 작은 경우
                # 우선순위가 더 낮은게 나올 때 까지 pop
                while stack and isp[stack[-1]] >= icp[data[i]]:
                    print(stack.pop(), end='')
                stack.append(data[i]) 
                # 위의 while 통해 우선순위가 낮아지거나 비워지게 됨
# 수식을 다 읽었을 때 stack에 연산자가 남아 있으면 pop() 하면서 출력
while stack:
    print(stack.pop(), end='')