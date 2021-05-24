from itertools import count
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for num in nums:
            if num == 0:
                nums.pop(nums.index(num))
                nums.append(num)

        print(nums)

if __name__ == '__main__' :
    nums = [4,2,4,0,0,3,0,5,1,0]
    solution = Solution()
    a = solution.moveZeroes(nums)
    # print(a)