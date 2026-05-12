class MinStack:

    def __init__(self):
        self.stack = []      # 存正常數字
        self.minStack = []   # 存每一層當下的最小值

    def push(self, val: int) -> None:
        if len(self.minStack) == 0:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            if val < self.minStack[-1]:
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        if len(self.stack):
            del self.stack[-1]
            del self.minStack[-1]
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
