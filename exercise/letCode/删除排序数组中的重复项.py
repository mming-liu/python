from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # for num in nums:
        #     num_index = nums.index(num)
        #     if num_index < len(nums)-1:
        #         if num == nums[num_index+1]:
        #             nums.remove(num)
        #         print(nums)

        # for i in range(len(nums)-2,-1,-1):
        # # 删除元素后，数组的长度会随之改变，所以从末尾开始循环
        #     if nums[i] == nums[i+1]:
        #         nums.remove(nums[i])

        num2=nums.copy()
        for i in num2:
            if(int(nums.count(i))==1):
                continue 
            else:
                nums.remove(i)
        # return len(nums)
        return nums

if __name__ == '__main__':
    nums = [1,1,1,1]
    solution = Solution()
    deal_nums = solution.removeDuplicates(nums)
    print(len(deal_nums),deal_nums)