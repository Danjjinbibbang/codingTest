N = int(input())

# Please write your code here.
def print_cnt(n, cnt):
    if(n == 1):
        return cnt
    cnt += 1
    if(n % 2 == 0):
        n //= 2
    else:
        n //= 3
    return print_cnt(n, cnt)
print(print_cnt(N, 0))