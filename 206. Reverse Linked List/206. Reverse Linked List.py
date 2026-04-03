#
# Problem: 206. Reverse Linked List
# Difficulty: Easy
# Link: https://leetcode.com/problems/reverse-linked-list/submissions/1967260619/
# Language: python3
# Date: 2026-04-03


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
