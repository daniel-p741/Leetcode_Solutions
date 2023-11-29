s = "   fly me   to   the moon  "


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.title()
        last = [i for i, x in enumerate(s) if x.isupper()][-1]
        return len(s[last:].replace(" ", ""))


Example = Solution()

Output = Example.lengthOfLastWord(s)

print(Output)
