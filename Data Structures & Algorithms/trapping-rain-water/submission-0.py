class Solution:
    def trap(self, height: List[int]) -> int:
        # 哪邊比較矮，就先處理哪邊
        # 因為矮的那邊會決定目前能裝多少水
        l = 0
        r = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        
        ans = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans