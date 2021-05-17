import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set有去重效果，数组交集中有多个相同元素时，只返回一个，不适用
        # return set(nums1).intersection(set(nums2))

        # 由于同一个数字在两个数组中都可能出现多次，因此需要用哈希表存储每个数字出现的次数。对于一个数字，
        # 其在交集中出现的次数等于该数字在两个数组中出现次数的最小值。首先遍历第一个数组，并在哈希表中记录
        # 第一个数组中的每个数字以及对应出现的次数，然后遍历第二个数组，对于第二个数组中的每个数字，
        # 如果在哈希表中存在这个数字，则将该数字添加到答案，并减少哈希表中该数字出现的次数。
        # 为了降低空间复杂度，首先遍历较短的数组并在哈希表中记录每个数字以及对应出现的次数，
        # 然后遍历较长的数组得到交集。

        if len(nums1) < len(nums2):
            return self.intersect(nums2,nums1)

        # 根据官方思路自己写出来的
        # dict = {}
        # list = []
        # for num1 in nums1:
        #     dict[num1] = nums1.count(num1)
        
        # for num2 in nums2:
        #     if num2 in dict.keys(): 
        #         dict[num2] = dict[num2] - 1              
        #         if dict[num2] >= 0:
        #             list.append(num2) 
        
        # return list

        # 官方解法
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        
        intersection = list()
        for num in nums2:
            count = m.get(num, 0)
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        
        return intersection

if __name__ == '__main__' :
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    # nums1 = [1,2,2,1]
    # nums2 = [2,2]
    solution = Solution()
    a = solution.intersect(nums1,nums2)
    print(a)