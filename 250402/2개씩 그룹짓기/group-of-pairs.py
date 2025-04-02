n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
# nums를 오름차순 정렬
# nums의 양 끝 원소를 합한 list => sum_nums
# sum_nums의 원소 중 최댓값 출력
nums.sort()
sum_nums = []

for i in range(len(nums)//2):
    sum_nums.append(nums[i] + nums[len(nums)- i - 1])
sum_nums.sort(reverse=True)

print(sum_nums[0])
