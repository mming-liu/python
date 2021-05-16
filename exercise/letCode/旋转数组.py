from typing import List
from operator import itemgetter
import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # dict = {}
        # k = k // len(nums)
        # for i,num in enumerate(nums):
        #     m = i + k
        #     if m >= len(nums):
        #         m = m - len(nums) 
        #     dict[m] = num
        # new_dict = sorted(dict.items())
        # # print(type(new_dict),new_dict)
        # # list = []
        # for i in new_dict:
        #     m = i[1]
        #     n = i[0]
        #     nums[n] = m
        # print(nums)

        # # 官方解法1：利用临时数组
        # tmp_list = []
        # k = k % len(nums)
        # for i in range(len(nums)):
        #     tmp_list.append(nums[(i + k) % len(nums)])
                
        # for i in range(len(nums)):
        #     nums[i] = tmp_list[i]
        # print(nums)

        # 官方解法2：环状替换
        k = k % len(nums)
        # count = math.gcd(k,len(nums))
        for i in range(len(nums)):
            tmp = nums[i]
            nums[i] = nums[(i + k) % len(nums)]
            nums[(i + k) % len(nums)] = tmp
        print(nums)              

if __name__ == '__main__' :
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    a = solution.rotate(nums,k)
    # print(a)