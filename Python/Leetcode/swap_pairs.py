class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
  def swapPairs(self, head):
    len = 0
    curr = head
    while curr != None:
      curr = curr.next
      len += 1
    
      