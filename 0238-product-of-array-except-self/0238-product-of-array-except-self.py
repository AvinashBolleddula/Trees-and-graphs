class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = [1] * n
        right_product = [1] * n
        results = [1] * n

        left_product[0], right_product[-1] = nums[0], nums[-1]

        for i in range(1, n):
            left_product[i] = nums[i] * left_product[i - 1]
        for i in range(n - 2, -1, -1):
            right_product[i] = nums[i] * right_product[i + 1]

        for i in range(n):
            if i == 0:
                results[i] = right_product[i + 1]
            elif i == n - 1:
                results[i] = left_product[i - 1]
            else:
                results[i] = left_product[i - 1] * right_product[i + 1]

        return results
