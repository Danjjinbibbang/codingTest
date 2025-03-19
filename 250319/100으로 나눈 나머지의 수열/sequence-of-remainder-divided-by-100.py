N = int(input())

# Please write your code here.
def print_num(n):
    if(n == 1):
        return 2
    if(n == 2):
        return 4
    return print_num(n-2) * print_num(n-1) % 100
print(print_num(N))
