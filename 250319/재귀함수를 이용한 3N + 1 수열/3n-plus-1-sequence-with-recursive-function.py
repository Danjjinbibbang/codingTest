n = int(input())

# Please write your code here.
def print_num(n, cnt):
    if(n == 1):
        return cnt
    cnt += 1
    if(n % 2 == 0):
        return print_num(n // 2, cnt)
    else:
        return print_num(n * 3 + 1, cnt)
print(print_num(n, 0))