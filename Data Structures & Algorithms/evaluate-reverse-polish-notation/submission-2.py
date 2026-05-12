class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 數字丟stack 遇到符號就相加再丟進去
        stack = []
        ans = 0
        for s in tokens:
            if s == '+' or s == '-' or s == '*' or s == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                if s == '+':
                    stack.append(str(b + a))
                if s == '-':
                    stack.append(str(b - a))
                if s == '*':
                    stack.append(str(b * a))
                if s == '/':
                    stack.append(str(int(b / a)))
            else:
                stack.append(s)
        
        return int(stack.pop())
