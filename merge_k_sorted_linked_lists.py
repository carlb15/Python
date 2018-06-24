# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        O(n*log(k)) Time where k is the number of Linked lists
                  O(logk) for the priority queue and N nodes in the final LL.
        O(k) Space - priority queue (often implemented with heaps)
                     costs O(k) space (it's far less than N in most situations).
        """
        lists = [x for x in lists if x]
        if not lists:
            return None
        
        queue = []
        for node in lists:
            if node:
                heapq.heappush(queue, (node.val, id(node), node))        

        dummy_head = curr = ListNode(-1)
        while queue:
            curr.next = heapq.heappop(queue)[2]
            curr = curr.next
            if curr.next:
                heapq.heappush(queue, (curr.next.val, id(curr.next), curr.next))

        return dummy_head.next     


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy_head = curr = ListNode(None)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return dummy_head.next        

'==================Merge with Divide And Conquer ========================'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution:
    def mergeTwoLists(self, list1, list2):
        """Merge two lists in O(n) time and O(1) space"""
        dummy_head = curr = ListNode(None)
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return dummy_head.next        


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        O(nlog(k)) time O(1) space
        """
        lists = [x for x in lists if x]
        if not lists:
            return lists
        
        num_lists = len(lists)
        interval  = 1
        
        # O(log(k)) times 
        while interval < num_lists:                    
            for idx in range(0, num_lists - interval, interval*2 ):
                # O(n) time
                lists[idx] = self.mergeTwoLists(lists[idx], lists[idx + interval])
            interval *= 2
        return lists[0] if num_lists > 0 else lists
        
        