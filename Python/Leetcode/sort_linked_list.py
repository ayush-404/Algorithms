# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#https://leetcode.com/problems/sort-list/submissions/
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
          return None
        curr = head
        arr = []
        while curr!= None:
          arr.append(curr.val)
          curr = curr.next
        arr.sort()
        Head = ListNode(arr[0])
        curr = Head
        for i in range(1, len(arr)):
          NewNode = ListNode(arr[i])
          curr.next = NewNode
          curr = NewNode
        return Head
