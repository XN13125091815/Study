class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = 0
        while i < len(nums):
            while j < i:
                if nums[i] + nums[j] == target:
                    return [j, i]
                j += 1
            i += 1


if __name__ == "__main__":
    solution = Solution()
    arr = solution.twoSum(nums=[1, 5, 6, 1, 8], target=6)
    print(arr)
