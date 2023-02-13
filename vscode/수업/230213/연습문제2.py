# s = '(asdsad(dd)sadd)'
s = input()

# #stack
# stack = []
# count = 0
# for i in s:
#     if i == '(':
#         stack.append(i)
#     if i == ')':
#         if len(stack) != 0:
#             stack.pop()
#             count += 1
# print(count)

# import stack_test as st

# count = 0
# stack = st.MyStack(5)
# for i in s:
#     if i == '(':
#         stack.push(i)
#     if i == ')':
#         stack.pop()
#         count += 1
# print(count)

#############
data = input()

def check_bracket(data):
    stack = []
    for c in data:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack: # stack이 비어있을 때
                return False # 짝 안맞음
            stack.pop()
    # 반복문이 끝났을 때, 괄호 짝이 맞았으면 스택이 비어있을 것
    if stack:   # 다 끝났는데 비어있지 않으면
        return False
    # 괄호가 남지 않았다
    return True

result = check_bracket(data)
print(result)