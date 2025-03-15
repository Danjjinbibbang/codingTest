n = int(input())

# Please write your code here.
def print_start(n):
    if(n == 0):
        return
    print('HelloWorld')
    print_start(n-1)

print_start(n)