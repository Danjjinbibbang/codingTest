N = int(input())

# Please write your code here.
def print_pow(n):
    if(n < 10):
        return pow(n, 2)
    return pow((n % 10), 2) + print_pow(n // 10)
print(print_pow(N))
