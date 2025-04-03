n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
# 문자열 t로 시작하는 단어를 필터링 startswith()
filtered = [word for word in str if word.startswith(t)]

filtered.sort()

print(filtered[k-1])