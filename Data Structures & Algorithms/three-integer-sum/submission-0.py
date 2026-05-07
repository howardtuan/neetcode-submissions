class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # 避免固定到重複的第一個數
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    l += 1
                    r -= 1

                    # 避免重複的第二個數
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return res