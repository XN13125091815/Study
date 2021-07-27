class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
        strs = str(x)
        strsList = list(strs)
        strsList.reverse()
        if flag is True:
            strsList.remove('-')
        strs = "".join(str(item) for item in strsList)
        x = int(strs)
        if flag is True:
            x = -x
        return x


if __name__ == "__main__":
    solution = Solution()
    x = solution.reverse(x=1534236469)
    print(x)
