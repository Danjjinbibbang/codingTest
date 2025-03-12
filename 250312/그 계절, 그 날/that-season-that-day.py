Y, M, D = map(int, input().split())

# Please write your code here.

#윤년인지?
def is_leap():
    flag = False
    if(Y % 4 == 0):
        flag = True
        if(Y % 100 == 0):
            flag = False
            if(Y % 400 == 0):
                flag = True
    return flag

#입력 데이터에 대해서 있는 날짜인지?
def input_date(M, D):
    List_30 = [4, 6, 9, 11]
    List_31 = [1, 3, 5, 7, 8, 10, 12]

    for i in range (len(List_30)):
        if(List_30[i] == M):
            return 30

    for i in range (len(List_31)):
        if(List_31[i] == M):
            return 31

    if(M == 2 and is_leap()):
        return 29
    elif(not is_leap()):
        return 28

def is_date(M, D):
    if(M > 12 or D > 31):
        return False
    else:
        max_d = input_date(M, D)
        if(max_d < D):
            return False
    return True

def match_season():
    if(is_date(M, D)):
        if(M == 3 or M == 4 or M == 5):
            return "Spring"
        if(M == 6 or M == 7 or M == 8):
            return "Summer"
        if(M == 9 or M == 10 or M == 11):
            return "Fall"
        if(M == 12 or M == 1 or M == 2):
            return "Winter"
    else:
        return "-1"

print(match_season())

