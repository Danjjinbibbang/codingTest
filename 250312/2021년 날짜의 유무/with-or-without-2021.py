M, D = map(int, input().split())

# Please write your code here.
def input_date(M, D):
    List_30 = [4, 6, 9, 11]
    List_31 = [1, 3, 5, 7, 8, 10, 12]

    for i in range (len(List_30)):
        if(List_30[i] == M):
            return 30

    for i in range (len(List_31)):
        if(List_31[i] == M):
            return 31

    if(M == 2):
        return 28

def is_date(M, D):
    if(M > 12 or D > 31):
        return False
    else:
        max_d = input_date(M, D)
        if(max_d < D):
            return False
    return True
            
if(is_date(M, D)):
    print("Yes")
else:
    print("No")


            
