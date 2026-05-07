class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 傳回一個單一字母的最長字串 長度

        # r 一直往右擴張
        # 用 hashmap/count 記錄每個字母出現次數
        # 維護目前視窗中「出現最多次的字母數量」
        # 如果需要修改的字母數超過 k , window_size - max_freq <= k
        #   就移動 l

        l = 0
        r = 0
        MyDict = {}
        ans = 0
        max_freq = 0
        for r in range(len(s)):
            # 1. 把 s[r] 加進 dict
            MyDict[s[r]] = MyDict.get(s[r],0) + 1
            # 2. 更新 max_freq
            max_freq = max(max_freq,MyDict[s[r]])
            # 3. 如果不合法，就移動 l
            window_size = r - l + 1
            if window_size - max_freq > k:
                MyDict[s[l]] -= 1
                l += 1
            # 4. 更新 ans
            ans = max(ans, r - l + 1)
        return ans
