class Solution:
    def __init__(self):
        self.triplets = []

    def find_triplets_with_zero_sum(self, nums,target):
        sorted_array = sorted(nums)
        TripleNums = set()
        for i in range(len(nums)-2):
            left , right = i+1,len(nums)-1
            while left < right:
                sum = sorted_array[i] +  sorted_array[left] + sorted_array[right]
                if  sum>target:
                    right-=1
                elif sum<target:
                    left+=1
                else:
                    TripleNums.add((sorted_array[i],sorted_array[left],sorted_array[right]))
                    left+=1
                    right-=1
        return TripleNums

solution = Solution()
nums = [-1, 0, 1, 2, -1, -4, -3, 3, 1]
result = solution.find_triplets_with_zero_sum(nums,4)
print(result)