class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right = 0
        left = 0
        for i in range(len(nums)):
            j = i+1
            while(j<len(nums)):
                right+=nums[j]
                j+=1
            if right == left:
                return i
            else:
                left+=nums[i]
                right = 0
        return -1
