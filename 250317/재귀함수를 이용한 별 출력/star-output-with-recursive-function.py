n = int(input())

# Please write your code here.
def print_star(n):
    if(n == 0):
        return
    print_star(n-1)
    for i in range(n):
        print("*", end="")
    print()
print_star(n)