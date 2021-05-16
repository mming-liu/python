from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # set有去重效果，数组交集中有多个相同元素时，只返回一个，不适用
        # return set(nums1).intersection(set(nums2))

        # hashtable的key和value，是与正常的字典相反存储的
        hashtable = dict()
        count = 0
        list = []
        for num1 in enumerate(nums1):
            if num1 in hashtable:
                count = count + 1
            hashtable[num1] = count
        
        for num2 in nums2:
            if num2 in hashtable:
                list.append(num2)
        
        return list

if __name__ == '__main__' :
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    solution = Solution()
    a = solution.intersect(nums1,nums2)
    print(a)