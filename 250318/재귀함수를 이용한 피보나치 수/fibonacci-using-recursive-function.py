N = int(input())

# Please write your code here.
def print_num(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 1
    return print_num(n-2) + print_num(n-1)
print(print_num(N))