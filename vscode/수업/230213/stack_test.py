class MyStack:
    def __init__(self,length):
        self.s = [0]*length
        self.top = -1
    #만들어야할 기능
    # push,pop,peek, is_full, is_empty
    def push(self,data):
        #맨뒤에 집어 넣기
        if not self.is_full():
            self.top += 1
            self.s[self.top] = data
        else:
            raise IndexError('가득 차있습니다.')
    # 마지막요소를 삭제하면서 반환
    def pop(self):
        if not self.is_empty():
            last = self.top
            self.top -= 1
            return self.s[last]
        raise IndexError('스택이 비었습니다.')

    #현재 마지막요소 반환, 단 요소가 있으면 반환
    def peek(self):
        if not self.is_empty():
            return self.s[self.top]
        raise IndexError('스택이 비었습니다.')

    #가득차있으면 True, 아니면 False 반환
    def is_full(self):
        if self.top == len(self.s)-1:
            return True
        return False

    # 비어있으면 True, 아니면 False 반환
    def is_empty(self):
        if self.top == -1:
            return True
        return False


stack = MyStack(5)
stack.push(5)
stack.push(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(0)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())



