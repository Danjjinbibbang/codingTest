N = int(input())

# Please write your code here.
def print_list(n):
    if(n == 1):
        return 1
    if(n == 2):
        return 2
    return print_list(n // 3) + print_list(n-1)

print(print_list(N))