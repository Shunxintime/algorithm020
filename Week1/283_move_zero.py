# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
    # 1.把I不是0的给J，直到I走到头，补零给J剩下的路
#         j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j+=1
#         for i in range(j,len(nums)):
#             nums[i] = 0

class Solution:
    # 2. i遍历，j指向左边为0的位置。
    # def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[i],nums[j] = nums[j],nums[i]
                j+=1

