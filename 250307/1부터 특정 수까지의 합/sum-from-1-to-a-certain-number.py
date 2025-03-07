n = int(input())

# Please write your code here.
def print_num(n):
    i = 1
    sum = 0
    result = 0

    while(i <= n):
        sum += i
        i += 1

    print(int(sum / 10))

print_num(n)