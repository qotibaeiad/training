class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        index = 1  # Start from the second element
        cnt = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                nums[index] = nums[i]
                index += 1
        for i in range(len(nums) - cnt,len(nums)):
            nums[i]=None
        print(nums)
        return cnt

s = Solution()
arr = [1,1,1,1,1,4,2,2,2,2]
print(s.removeDuplicates(arr))
