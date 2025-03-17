N = int(input())

# Please write your code here.
def print_flower(n):
    if(n == 0):
        return
    print(n, end=" ")
    print_flower(n-1)
    print(n, end=" ")

print_flower(N)