a, b = map(int, input().split())

# Please write your code here.
def num_3(a, b):
    count = 0
    for i in range(a, b+1):
        if(i % 3 == 0):
            count += 1
            #print("3의 배수: ", i)
    return count
    #print(count)

def num_369(a, b):
    count = 0
    for i in range(a, b+1):
        if(i < 10):
            continue
        if(i % 3 != 0): # 3의 배수가 아닐때만 자리에 3 6 9가 포함되는 확인
            while(i // 10 != 0):
                if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
                    #print("3 6 9: ", i)
                    count += 1
                    break
                i = i // 10
            if(i == 3 or i ==6 or i==9):
                #print("한자리: ", i)
                count += 1
    return count
    #print(count)

def print_result(a, b):
    result1 = num_3(a, b)
    result2 = num_369(a, b)
    result = result1 + result2
    print(result)

print_result(a, b)
