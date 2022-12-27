class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            min = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min]:
                    min = j
            nums[i],nums[min] = nums[min],nums[i]
            if nums[i] == target:
                ans.append(i)
        return ans
