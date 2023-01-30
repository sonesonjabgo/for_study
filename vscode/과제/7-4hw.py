def collatz(num):
    result = 0
    while num != 1:
        result += 1
        if result == 500:
            result = -1
            break

        if num % 2:
            num = num * 3 + 1
        else:
            num = num / 2
    print(result)




collatz(6)  # => 8
collatz(16)  # => 4
collatz(27)  # => 111
collatz(626331)  # => -1
