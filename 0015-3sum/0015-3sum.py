class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        dup = set()

        for i in range(len(nums)):
            if nums[i] in dup:
                continue
            dup.add(nums[i])

            seen = set()
            for j in range(i + 1, len(nums)):
                target = -nums[i] - nums[j]
                if target in seen:
                    res.add(tuple(sorted((nums[i], nums[j], target))))
                seen.add(nums[j])

        return [list(t) for t in res]