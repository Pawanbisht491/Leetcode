class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in dic:
                return [dic[c], i]
            dic[nums[i]] = i
        return []