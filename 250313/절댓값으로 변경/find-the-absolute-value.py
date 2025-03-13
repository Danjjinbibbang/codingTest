n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def abs_list(arr):
    for i in range(n):
        if(arr[i] < 0):
            arr[i] *= -1

abs_list(arr)
for i in range(n):
    print(arr[i], end=" ")