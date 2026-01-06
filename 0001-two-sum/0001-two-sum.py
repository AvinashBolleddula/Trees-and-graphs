from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i,num in enumerate(nums):
            if target - num in mapp:
                return [i,mapp[target-num]]
            mapp[num] = i


        