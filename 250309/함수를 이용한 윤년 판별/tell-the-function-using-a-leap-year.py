y = int(input())

# Please write your code here.
# 윤년 판별
def leap_year(y):
    if(y % 100 == 0 and y % 400 != 0):
        return False
    if(y % 4 == 0):
        return True

if(leap_year(y)):
    print("true")
else:
    print("false")
