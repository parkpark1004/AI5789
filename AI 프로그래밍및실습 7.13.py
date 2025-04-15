#7.13

nums = [5, 6, 3, 9, 2, 12, 3, 8, 7]
print('주어진 리스트는=', nums)

n = len(nums)
for i in range(n):
    for j in range(1, n - i):
        if nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]

print('정렬된 결과는', nums)
