class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums  = sorted(nums)
        min_diff = float('inf')
        ans = 0
        for i in range(len(nums)-2):
            low = i+1
            high = len(nums)-1
            while low < high:
                diff = abs(target - (nums[i] + nums[low] + nums[high]))
                if diff < min_diff:
                    min_diff = diff
                    ans = nums[i] + nums[low] + nums[high]
                if nums[i] + nums[low] + nums[high] < target:
                    low+=1
                elif nums[i] + nums[low] + nums[high] > target:
                    high-=1
                else:
                    return target
        return ans
    

       