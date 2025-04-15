#5.9

def mean_of_n(nums):
    return sum(nums) / len(nums)

def max_of_n(nums):
    return max(nums)

def min_of_n(nums):
    return min(nums)

입력 = input("정수를 여러 개 입력하시오: ")
nums = list(map(int, 입력.split()))

print("평균값은", mean_of_n(nums))
print("최댓값은", max_of_n(nums))
print("최솟값은", min_of_n(nums))
