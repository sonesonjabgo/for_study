class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x + self.y)
    
    def substract(self):
        print(self.x - self.y)
    
    def multuply(self):
        print(self.x * self.y)
    
    def divide(self):
        try:
            print(self.x / self.y)
        
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다.')
            
# 1 + 2
cal = Calculator(1, 2)
cal.add()

# 2 – 1
cal = Calculator(2, 1)
cal.substract()

# 3 * 4
cal = Calculator(3, 4)
cal.multuply()

# 4 / 0
cal = Calculator(4, 0)
cal.divide()