class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 1:
            return nums[length // 2]
        else:
            Sum = nums[length // 2 - 1] + nums[length // 2]
            return Sum / 2
            # if len(nums) <= 2:
            #     Sum = nums[length // 2 - 1] + nums[length // 2]
            #     return Sum / 2
            # else:
            #     Sum = nums[(length // 2) - 1] + nums[length // 2]
            #     return Sum / 2


if __name__ == "__main__":
    solution = Solution()
    Median = solution.findMedianSortedArrays(nums1=[1, 2], nums2=[5, 6])
    print(Median)
