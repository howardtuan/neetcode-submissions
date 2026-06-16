class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid_index = (l + r) // 2
            # mid = (nums[l] + nums[r]) // 2
            if target < nums[mid_index]:
                r = mid_index - 1
            elif target > nums[mid_index]:
                l = mid_index + 1
            else:
                return mid_index
        return -1