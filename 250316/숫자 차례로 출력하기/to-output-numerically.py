n = int(input())

# Please write your code here.

def print_1(n, i=1):  # i를 인자로 받아 전역 변수 사용 제거
    if i > n:  # 종료 조건 추가
        print()
        print_2(n)
        return  # 재귀 종료
    print(i, end=" ")
    print_1(n, i + 1)  # i를 증가시키며 재귀 호출

def print_2(n):
    if n == 0:  # 종료 조건
        return
    print(n, end=" ")
    print_2(n - 1)  # 재귀적으로 감소

print_1(n)
