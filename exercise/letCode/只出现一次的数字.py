from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # for num in nums :
        #     if nums.count(num) == 1:
        #         return num

        # reduce（函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
        #       用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
        #       得到的结果再与第三个数据用 function 函数运算，最后得到一个结果）：
        #        https://www.runoob.com/python/python-func-reduce.html
        # "^" :异或
        # 任何数和 0 做异或运算，结果仍然是原来的数，即 a⊕0=a。
        # 任何数和其自身做异或运算，结果是 0，即 a⊕a=0。
        # 异或运算满足交换律和结合律，即 a⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

        # 官方解法
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == '__main__' :
    nums = [4,1,2,1,2]
    solution = Solution()
    a = solution.singleNumber(nums)
    print(a)