class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        intList = []
        i = 0
        num = 0
        if s == "" or s == "+" or s == "-":
            return 0
        flag = True
        while i < len(s):
            if s[i] == '+' and i == 0:
                flag = True
                i += 1
            elif s[i] == '-' and i == 0:
                flag = False
                i += 1
            elif (s[i].isalpha() or s[i] == '.') and i == 0:
                return 0
            elif (s[i] == '+' or s[i] == '-' or s[i] == ' ' or s[i].isalpha()) and i == 1 and (s[0] == '+' or s[0] == '-'):
                return 0
            elif (s[i].isalpha() or s[i] == '.' or s[i] == ' ' or s[i] == '-' or s[i] == '+') and i != 0:
                break
            elif s[i].isdigit():
                intList.append(s[i])
                i += 1
        strs = "".join(str(item) for item in intList)
        num = getnum(strs=strs, flag=flag)
        return num


def getnum(strs: str, flag: bool) -> int:
    if flag:
        num = int(strs)
    else:
        num = -int(strs)
    if num > 2 ** 31 - 1:
        num = 2 ** 31 - 1
    elif num < (-2) ** 31:
        num = (-2) ** 31
    return num


if __name__ == "__main__":
    solution = Solution()
    num = solution.myAtoi(s="-adf")
    print(num)
