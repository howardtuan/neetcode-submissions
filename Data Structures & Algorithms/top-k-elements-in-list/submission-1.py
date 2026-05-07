class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket Sort
        count = Counter(nums)
        print(count)
        print(count.items())
        # bucket index = 出現次數
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for num,freq in count.items():
            bucket[freq].append(num)

        print(bucket)
        ans = []
        # 從高頻往下找(由後到前)
        for i in range(len(bucket) - 1 , 0 , -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        return ans