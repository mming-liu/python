from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # s = 0
        # list = []
        # for i in range(len(digits)):
        #     s = s + digits[i] * pow(10,len(digits)-i-1)

        # s = str(s + 1)

        # for i in s:
        #     list.append(int(i))
        
        # return list

        num = int(''.join([str(s) for s in digits]))+1
        return [int(s) for s in str(num)]

if __name__ == '__main__' :
    digits = [1,2,3]
    solution = Solution()
    a = solution.plusOne(digits)
    print(a)
