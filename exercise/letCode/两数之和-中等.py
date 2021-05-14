# Definition for singly-linked list.
# from typing import ListNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sums = []
        for i in range(len(l1)):
            for j in range(i+1,len(l1)):
                sum = l1[i] + l1[j]
                sums.append(sum)
        
        for i in range(len(sums)):
            for j in range(len(l2)):
                if sums[i] == l2[j]:
                    return j

if __name__ == '__main__' :
    l1 = [2,4,3]
    l2 = [5,6,4]
    solution = Solution()
    a = solution.addTwoNumbers(l1,l2)
    print(a)