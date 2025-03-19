a, b, c = map(int, input().split())

# Please write your code here.
inter = a * b * c
def print_sum(n):
    if(n < 10):
        return n
    return n % 10 + print_sum(n // 10)

print(print_sum(inter))