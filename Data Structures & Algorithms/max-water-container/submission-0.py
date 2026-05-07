class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        while l < r:
            # 計算面積

            # if heights[l] * heights[r] > ans:
            #     ans = heights[l] * heights[r]
        
            if heights[l] < heights[r]:
                temp = heights[l] * (r - l)
                if temp > ans:
                    ans = temp
                l += 1
            else :
                temp = heights[r] * (r - l)
                if temp > ans:
                    ans = temp
                r -= 1
        return ans