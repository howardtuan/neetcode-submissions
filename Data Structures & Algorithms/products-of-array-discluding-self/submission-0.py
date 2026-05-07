class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 每個位置的答案 =「左邊全部乘起來」 × 「右邊全部乘起來」
        ans = [1] * len(nums)
        # 第一圈：ans[i] 先放「左邊乘積」
        left = 1
        for i in range(len(nums)):
            ans[i] = left
            left *= nums[i]
        # 第二圈：再乘上「右邊乘積」
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans