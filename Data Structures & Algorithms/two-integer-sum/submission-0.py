class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        MyDict = {}
        for i in range(0,len(nums)):
            complement = target - nums[i]
            if complement in MyDict:
                ans.append(MyDict[complement])
                ans.append(i)
                return ans
            MyDict[nums[i]] = i

        return ans