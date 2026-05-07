class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 要先想辦法把標點符號與空格都移除 只保留英文跟數字
        # 是字母就把它換成小寫
        left = 0
        right = len(s) - 1
        
        while left <= right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
