class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # 如果字符串列表為空，返回空字符串
            return ""
        prefix = strs[0]

        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""

        return prefix
