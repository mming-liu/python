from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    list.append(i)
                    list.append(j)
                    return list

if __name__ == '__main__' :
    nums = [3,2,4]
    target = 6
    solution = Solution()
    a = solution.twoSum(nums,target)
    print(a)