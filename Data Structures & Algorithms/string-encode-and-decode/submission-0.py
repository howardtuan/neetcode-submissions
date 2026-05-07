class Solution:

    def encode(self, strs: List[str]) -> str:
        # "len1#str1len2#str2..."
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
    def decode(self, s: str) -> List[str]:
        print('s = ',s)
        i = 0
        n = len(s)
        res = []
        while i < n:
            # 找到最前面的 # 讀取長度
            j = s.find('#', i)
            if j == -1:
                # 格式有誤
                break
            length = int(s[i:j]) # len
            val_start = j + 1 # str起點
            val_end = val_start + length # str終點
            res.append(s[val_start:val_end])
            i = val_end
        return res