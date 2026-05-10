class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # 存 index，不是存數字
        res = []
        l = 0

        for r in range(len(nums)):

            # 1. 新來的 nums[r] 如果比較大
            # 就把前面比它小的都丟掉
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # 2. 把目前位置放進去
            q.append(r)

            # 3. 如果最左邊的 index 已經不在視窗內，就丟掉
            if q[0] < l:
                q.popleft()

            # 4. 視窗大小到 k，才開始收答案
            if r - l + 1 == k:
                res.append(nums[q[0]])  # q[0] 就是最大值的位置
                l += 1

        return res