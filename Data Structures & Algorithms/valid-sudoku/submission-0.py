class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]# rows[0]：第 0 列出現過哪些數字 
        cols = [set() for _ in range(9)]# cols[0]：第 0 行出現過哪些數字 
        boxes = [set() for _ in range(9)]# boxes[0]：第 0 個 3x3 宮格出現過哪些數字
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                box_index = (r // 3) * 3 + (c // 3)
                # 某格是哪個 3 * 3 ? (r // 3, c // 3)
                if val in rows[r]:
                    return False
                if val in cols[c]:
                    return False
                if val in boxes[box_index]:
                    return False
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True