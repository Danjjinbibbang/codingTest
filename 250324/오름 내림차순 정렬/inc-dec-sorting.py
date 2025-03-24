n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
nums1 = nums[::-1]

for i in range(n):
    print(nums[i], end=" ")
print()
for i in range(n):
    print(nums1[i], end=" ")