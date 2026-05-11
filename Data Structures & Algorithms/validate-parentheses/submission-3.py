class Solution:
    def isValid(self, s: str) -> bool:
        MyDict = {'(':')','{':'}','[':']'}
        stack = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                temp = stack.pop()
                if s[i] != MyDict[temp]:
                    return False

        return len(stack) == 0