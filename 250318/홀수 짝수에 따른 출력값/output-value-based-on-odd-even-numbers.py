N = int(input())

# Please write your code here.
def print_num(n):
    if(n == 1 or n == 2):
        return n
    return n + print_num(n-2)
print(print_num(N))