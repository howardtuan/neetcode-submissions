class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # key: sorted string, value: list of anagrams

        for eachStr in strs:
            key = "".join(sorted(eachStr))  # 轉成字串
            if key not in groups:
                groups[key] = []

            groups[key].append(eachStr)

        return list(groups.values())