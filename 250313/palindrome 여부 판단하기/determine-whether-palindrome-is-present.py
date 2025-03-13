A = input()

# Please write your code here.
# 문자열 -> 배열로 변환
# 배열의 길이 -> 반으로 나눠서 대칭으로 원소를 변경함
# i len(list)-i-1 반복문 조건: i < len(list)-1-i
def is_palindrome(s):
    list_str = list(s)
    i = 0
    while(i < len(list_str)-1-i):
        list_str[i], list_str[len(list_str)-1-i] = list_str[len(list_str)-1-i], list_str[i]
        i += 1
    if("".join(list_str) == s):
        return True
    return False
if(is_palindrome(A)):
    print('Yes')
else:
    print('No')