class Solution:
    def convert(self, s: str, numRows: int) -> list:
        length = len(s)
        nums = length // numRows
        strlist = []
        i = 1
        everylen = 0
        while i <= nums:
            strlist.append(s[everylen:(everylen + numRows)])
            # if i == 3:
            #     break
            everylen += numRows
            i += 1
        strlist.append(s[everylen:])
        return strlist


if __name__ == "__main__":
    solution = Solution()
    ls = solution.convert(s="asaravadrgadfgergadsfgr", numRows=3)
    print(ls)
