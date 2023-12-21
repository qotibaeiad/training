def FindMissingNumber(nums):
    n = len(nums) + 1 
    expected_sum = n * (n + 1) // 2  

    actual_sum = sum(nums)

    return expected_sum - actual_sum


numbers = [1, 2, 4, 6, 3, 7, 8]
MissNum = FindMissingNumber(numbers)
print(f"missing number: {MissNum}")