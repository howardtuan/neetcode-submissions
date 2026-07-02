class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        cycle = False

        # O(N)
        while not cycle:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                cycle = True
        
        slow = 0
        # O(N)
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow