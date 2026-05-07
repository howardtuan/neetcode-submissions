class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        MyDict={}
        for i in range(len(nums)):
            if MyDict.get(nums[i])==None:
                MyDict[nums[i]]=1
            else:
                return True
        return False
