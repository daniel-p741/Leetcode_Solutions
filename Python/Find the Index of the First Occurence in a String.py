haystack = "sadbutsad"
needle = "sad"


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


Example = Solution()

Output = Solution.strStr(haystack, needle)

print(Output)
