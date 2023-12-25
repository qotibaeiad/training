class Solution(object):
    def twoSum(self, numbers, target):
        left,right = 0,len(numbers)-1
        while left<right:
            sum = numbers[left]+numbers[right]
            if sum==target:
                return [left+1,right+1]
            elif sum<target:
                left+=1
            else:
                right-=1
g = Solution()
print(g.twoSum([1,2,4,5,6,7,8],0))