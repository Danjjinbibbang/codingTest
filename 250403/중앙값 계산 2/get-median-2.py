n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 인덱스가 짝수일 때 중앙 값을 구해야 함
# 인덱스가 짝수일 때 마다 해당 인덱스/2 원소 값을 구해야 함
arr_center = []
for i in range(len(arr)):
    if(i % 2 == 0):
        arr_center = arr[0:i+1]
        arr_center.sort()
        print(arr_center[i//2], end=' ')
