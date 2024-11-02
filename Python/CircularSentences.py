sentence = "leetcode exercises sound delightful"


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        parts = sentence.split(" ")
        temp_list = []
        if len(parts) > 1:
            for i in range(len(parts) - 1):
                if (
                    i < len(parts) - 1
                    and parts[i][-1] == parts[i + 1][0]
                    and parts[0][0] == parts[-1][-1]
                ):
                    temp_list.append(True)
                else:
                    temp_list.append(False)
        else:
            if parts[0][0] == parts[0][-1]:
                temp_list.append(True)
            else:
                temp_list.append(False)

        if False not in temp_list:
            return True
        else:
            return False


Example = Solution()

Output = Example.isCircularSentence(sentence)

print(Output)
