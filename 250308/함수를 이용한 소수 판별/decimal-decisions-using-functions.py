a, b = map(int, input().split())

# Please write your code here.

# 소수
def is_prime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

# a~b 반복
def num(a, b):
    sum = 0
    for i in range(a, b+1):
        if (is_prime(i)):
            sum += i
    print(sum)

num(a, b)