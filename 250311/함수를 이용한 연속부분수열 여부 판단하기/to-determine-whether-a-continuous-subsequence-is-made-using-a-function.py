n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
# n1 > n2
# n1에 대해서 n2를 탐색하면서 n1의 원소와 n2의 원소가 같다면 다음 원소 비교
# 연달아서 같다면 Yes 출력

def search_list(a, b, n1, n2):
    if(n2 == 1):
        for i in range(n1):
            if(a[i] == b[0]):
                return True
    else:
        flag = False
        for i in range(len(a)):
            for j in range(len(b)):
                if(a[i] != b[j]):
                    flag = False
                else:
                    if(j == n2-1):
                        return flag
                    flag = True
                    if(i < n1-1):
                        i += 1
                    if(j < n2-1): 
                        j += 1
                        if(a[i] != b[j]):
                            return False                 
        return flag

def search_list1(a, b, n1):
    for i in range(n1):
        if(a[i] != b[i]):
            return False
    return True


if(n1 == n2):
    if(search_list1(a, b, n1)):
        print('Yes')
    else:
        print('No')


if(n1 > n2):
    if(search_list(a, b, n1, n2)):
        print('Yes')
    else:
        print('No')

if(n1 < n2):
    print('No')

