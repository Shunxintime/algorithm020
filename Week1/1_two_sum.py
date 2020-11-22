class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1 暴力搜索
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i] + nums[j] == target):
        #             return [i,j]
        # 2 找到那个剩下的朋友
        for i in range(len(nums)):
            j = target - nums[i]
            remain = nums[i + 1:]
            if j in remain:
                return [i, remain.index(j) + i + 1]