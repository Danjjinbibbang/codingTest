n = int(input())
arr = list(map(int, input().split()))
# Please write your code here.
def print_max(n, arr):
    if(n == 0):
        return arr[n]
    return max(print_max(n-1, arr), arr[n-1])
print(print_max(n, arr))