class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 先把所有數字放進 set
        # 走訪每個數字
        # 如果它是某段的起點（num - 1 不存在）
        # 就一路往後數有多長
        # 更新最長長度
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if num -1 not in nums_set: #是起點
                length = 1
                current = num
                while current + 1 in nums_set:
                    length += 1
                    current += 1
                longest = max(longest,length)
        return longest