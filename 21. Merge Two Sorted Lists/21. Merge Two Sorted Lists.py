#
# Problem: 21. Merge Two Sorted Lists
# Difficulty: Easy
# Link: https://leetcode.com/problems/merge-two-sorted-lists/submissions/2110709679/
# Language: python3
# Date: 2026-08-17


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        curr = newList

        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    curr.next = list1
                    list1 = list1.next
                elif list1.val > list2.val:
                    curr.next = list2
                    list2 = list2.next
                else:
                    curr.next = list1
                    list1 = list1.next
            elif not list1:
                curr.next = list2
                return newList.next
            else:
                curr.next = list1
                return newList.next
            curr = curr.next
        return newList.next
        
            



