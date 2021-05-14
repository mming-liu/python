from typing import List
from operator import itemgetter

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

        tmp_list = []
        tmp_len = len(nums)
        k = (k + 1 )% tmp_len
        for i in range(tmp_len):
            if i + k >= tmp_len  :
                tmp_list.append(nums[i+k-tmp_len])
            else:
                tmp_list.append(nums[i+k])
        for i in range(tmp_len):
            nums[i] = tmp_list[i]
        print(nums)

if __name__ == '__main__' :
    nums = [1,2,3,4,5,6,7]  
    k = 3
    solution = Solution()
    a = solution.rotate(nums,k)
    # print(a)