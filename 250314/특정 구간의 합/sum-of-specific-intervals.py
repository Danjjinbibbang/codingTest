n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def search_a1_a2():
    global arr
    
    for i in range(len(queries)):
        sum = 0
        a1 = queries[i][0]
        a1 -= 1
        a2 = queries[i][1]
        for j in range(a1, a2):
            sum += arr[j]
        print(sum)
search_a1_a2()