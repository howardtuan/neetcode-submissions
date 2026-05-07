class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        MyDict_s = {}
        MyDict_t = {}
        for i in range(len(s)):
            if MyDict_s.get(s[i]) == None:
                MyDict_s[s[i]] = 1
            else:
                MyDict_s[s[i]] += 1
            if MyDict_t.get(t[i]) == None:
                MyDict_t[t[i]] = 1
            else:
                MyDict_t[t[i]] += 1
        return MyDict_s == MyDict_t