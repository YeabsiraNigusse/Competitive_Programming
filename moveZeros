class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index1,index2 = 0 , 1
        size = len(nums)
        while(index2 < size):
          if nums[index1]==0 and nums[index2]!=0:
             nums[index1],nums[index2]=nums[index2],nums[index1]
             index1+=1
             index2+=1
          elif nums[index1] == 0 and nums[index2] ==0:
             index2+=1
          else:
             index1+=1
             index2+=1
        """ 
        Do not return anything, modify nums in-place instead.
        """
