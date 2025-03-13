A = input()

# Please write your code here.
# 문자열을 배열로 변환
# 배열을 순환하면서 겹치는 지 확인
# 겹치면 바로 return

def is_match(s):
    list_str = list(s)
    count = 0
    for i in range(len(list_str)):
        for j in range(i, len(list_str)):
            if(count >= 2):
                return True
            elif(list_str[i] != list_str[j]):
                count += 1
    return False

if(is_match(A)):
    print("Yes")
else:
    print("No")
