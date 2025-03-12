n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
# 리스트 슬라이싱..생각도 못함...gpt가 알려준 문제임..꼭 다시 풀어볼 것
# n1에 대해서 n2를 탐색하면서 n1의 원소와 n2의 원소가 같다면 다음 원소 비교
# 연달아서 같다면 Yes 출력

def search_list(a, b, n1, n2):
    for i in range(len(a) - len(b) + 1):
        if(a[i:i+len(b)] == b):
            return True
    return False

if(search_list(a, b, n1, n2)):
    print('Yes')
else:
    print('No')


