n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
# 인덱스가 아니라 n번째 원소임
def sum_elem(m):
    sum = 0
    while(m > 0):
        sum += A[m-1]
        if(m % 2 == 0):
            m //= 2
        else:
            m -= 1
    return sum

print(sum_elem(m))