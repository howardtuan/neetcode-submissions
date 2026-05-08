class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        t_count = {}
        window_count = {}
        for i in t:
            t_count[i] = t_count.get(i,0) + 1
        need = len(t_count)
        have = 0
        ans = ""
        for r in range(len(s)):
            window_count[s[r]] = window_count.get(s[r],0) + 1
            if s[r] in t_count and window_count[s[r]] == t_count[s[r]]:
                have += 1
            while have == need:
                if ans == "":
                    ans = s[l:r+1]
                elif len(ans) > len(s[l:r+1]):
                    ans = s[l:r+1]
                window_count[s[l]] = window_count.get(s[l]) - 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1

        return ans