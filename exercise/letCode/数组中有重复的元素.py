from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # count = 0
        # for num in nums:
        #     if nums.count(num) > 1:
        #         count = 1
        #         break
        #     else :
        #         pass
        
        # for num in nums:
        #         if nums.count(num) > 1:
        #             count = 1
        #             break

        # if count > 0 :
        #     return True
        # else:
        #     return False
        
        # set用来去重：https://www.runoob.com/python/python-func-set.html
        return len(nums) - len(set(nums)) > 0    

if __name__ == '__main__' :
    # nums = [1,2,3,4]
    # nums = [2,14,18,22,22]
    # nums = [1,2,3,1]
    nums = [0,4,5,0,3,6]
    solution = Solution()
    a = solution.containsDuplicate(nums)
    print(a)