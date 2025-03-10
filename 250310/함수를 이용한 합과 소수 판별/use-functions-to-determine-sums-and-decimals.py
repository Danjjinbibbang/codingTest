a, b = map(int, input().split())

# Please write your code here.
def add_place(n):
    sum = 0
    if(n <= 10):
        if(n == 2):
            return True
        else:
            return False
    while(n % 10 != 0):
        sum += n % 10
        n //= 10
    if(sum % 2 == 0):
        return True

def isPrime(n):
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True

count = 0
for i in range(a, b+1):
    if(add_place(i) and isPrime(i)):
        count += 1
print(count)
