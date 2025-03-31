n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

def match_list(A, B):
    for i in range(n):
        if(A[i] != B[i]):
           return False
    return True


if(not match_list(A, B)):
    print("No")
else:
    print("Yes")