n, m = map(int, input().split())

# Please write your code here.

numList = [n, m]
numList.sort()
n = numList[0]
m = numList[1]

def print_num(n, m):
    i = 2
    bothList = []
    result1 = 1
    result2 = 0

    while(i < m):
        if(n % i == 0 and m % i == 0):
            bothList.append(i)
        i += 1

    for j in range(len(bothList)):
        result1 *= bothList[j]
    #print("result1: ", result1)

    if(n // result1 == 0):
        print(result1)
        return
    else:
        result2 = n // result1
        result2 *= m
        print(result2)
        return

print_num(n, m)
