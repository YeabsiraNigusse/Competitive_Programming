class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prsum = {0:1}
        for i in nums:
            curSum += i
            diff = curSum - k
            res += prsum.get(diff,0)
            prsum[curSum] = 1 + prsum.get(curSum, 0)
        return res
