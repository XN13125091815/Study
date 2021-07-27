class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        strs = ""
        strlen = [0]
        if s == "":
            return 0
        # if len(s) == 1:
        #     return 1
        while i < len(s):
            while i <= j < len(s):
                if strs.find(s[j]) < 0:
                    strs += s[j]
                    j += 1
                else:
                    strlen.append(len(strs))
                    strs = s[j]
                    j += 1
            if j == len(s):
                strlen.append(len(strs))
            # if len(strs) == len(s):
            #     return len(s)
            strs = ""
            i += 1
            j = i
        return max(strlen)


if __name__ == "__main__":
    solution = Solution()
    s = input()
    Len = solution.lengthOfLongestSubstring(s)
    print(Len)
