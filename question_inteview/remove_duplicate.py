class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        index = 1  # Start from the second element
        cnt = 0
        currentnum=nums[0]
        for i in range(1, len(nums)):
            if nums[i] == currentnum:
                cnt += 1
                nums[i]=None
            else:
                currentnum = nums[i]
                nums[index] = nums[i]
                index += 1
        print(nums)
        return cnt

s = Solution()
arr = [1, 1, 2,2,2, 2, 3,3,3,3 ,3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
print(s.removeDuplicates(arr))
