class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {'+', '-', '*', '/'}

        for s in tokens:
            if s not in ops:
                stack.append(int(s))
            else:
                a = stack.pop()  # 右邊
                b = stack.pop()  # 左邊

                if s == '+':
                    stack.append(b + a)
                elif s == '-':
                    stack.append(b - a)
                elif s == '*':
                    stack.append(b * a)
                elif s == '/':
                    stack.append(int(b / a))

        return stack[-1]