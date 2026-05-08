class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # 用 slide window 去慢慢找有沒有符合的？
        if len(s1) > len(s2):
            return False
        l = 0
        s1_count = {}
        window_count = {}
        # 先統計 s1 算出 s1_count
        for s in s1:
            s1_count[s] = s1_count.get(s,0) + 1

        for r in range(len(s2)):
            window_count[s2[r]] = window_count.get(s2[r],0) + 1

            if r - l + 1 > len(s1):
                window_count[s2[l]] -= 1
                if window_count[s2[l]] == 0:
                    del window_count[s2[l]]
                l += 1
                
            if s1_count == window_count:
                return True
                
        
        return False
            