class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonmax_heapes = stones
        heapq.heapify_max(stonmax_heapes)
        print
        while len(stonmax_heapes) > 1:
            x = heapq.heappop_max(stonmax_heapes)
            y = heapq.heappop_max(stonmax_heapes)
        
            if x < y:
                heapq.heappush_max(stonmax_heapes, y - x)
            elif x > y:
                heapq.heappush_max(stonmax_heapes, x - y)
        if stonmax_heapes != []:
            return stonmax_heapes[0]
        return 0