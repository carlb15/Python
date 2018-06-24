"""
Sorting linked list in O(nlog(n)) Time, O(log(n)) Space
"""

# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
    def get_middle_node(self, head):
        slow, fast = head, head
        
        while fast.next and fast.next.next:            
            fast = fast.next.next
            slow = slow.next
        return slow

    
    def merge(self, left, right):
        dummy_head = curr = ListNode(None)
        
        while left and right:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        curr.next = left or right
        return dummy_head.next        
    
    
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        middle_node = self.get_middle_node(head)
        right = middle_node.next
        middle_node.next = None
        
        return self.merge(self.sortList(head), self.sortList(right))
        
        
    def createList(self, li):
      if not li or type(li) != list:
        raise ValueError("Lists of size 1 or greater required.")

      head = curr = ListNode(-1)

      for elem in li:
        curr.next = ListNode(elem)
        curr = curr.next
      return head.next
    
    
    def printList(self, head):
      if not head:
        print('Empty linked list')
        return head

      while head:
        print(head.val, end=' ')
        head = head.next
      print()


if __name__=="__main__":
  sol = Solution()
  head = sol.createList([4,2,1,3])
  sol.printList(head)
  head = sol.sortList(head)
  sol.printList(head)