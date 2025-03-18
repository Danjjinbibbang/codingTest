N = int(input())

# Please write your code here.
def pact(n):
    if(n == 1):
        return n
    return n * pact(n-1)
print(pact(N))