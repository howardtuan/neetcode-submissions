class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 兩台車交叉的的時候 在出發點比較遠的車一定會比較快(因為快才會追上去[交叉])
        cars = sorted(zip(position, speed), reverse=True)
        
        # 後車到終點的時間 <= 前車到終點的時間 代表後車可以追上前車 反之不行，就會變成獨立一個fleet
        
        stack = []

        for pos,spd in cars:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)