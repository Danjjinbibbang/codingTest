a, b = map(int, input().split())

# Please write your code here.
def cal_pow(a, b):
    result = 1
    if(a == 1):
        return 1
    elif(b == 1):
        return a
    else:
        for i in range(b):
            result *= a
        return result

resultCal = cal_pow(a, b)
print(resultCal)