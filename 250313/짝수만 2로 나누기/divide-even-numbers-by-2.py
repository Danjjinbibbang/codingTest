n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
# 새로운 리스트를 만들어서 넘긴다 list[:]
# 인수로 리스트를 넘기면 주소값이 넘어가기 때문에 리스트 내 원소 값 변경 시 반영됨
def div_even_nem(arr):
    for elem in range(len(arr)):
        if(arr[elem] % 2 == 0):
            arr[elem] //= 2
        print(arr[elem], end=" ")
    

div_even_nem(arr[:])