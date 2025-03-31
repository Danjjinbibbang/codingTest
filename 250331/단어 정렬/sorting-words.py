n = int(input())
word = [input() for _ in range(n)]

# Please write your code here.
#list.sort() 리턴값이 없음. sort()는 자체를 정렬함
#list.sorted() 새로운 list를 리턴함

word.sort()
for i in range(n):
    print(word[i])