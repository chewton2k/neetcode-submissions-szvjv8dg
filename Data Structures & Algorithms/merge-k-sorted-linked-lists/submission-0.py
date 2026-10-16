# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr_res = dummy
        heap = []

        for i, lst in enumerate(lists):
            curr = lst
            while curr is not None: 
                heap.append((curr.val, len(heap), curr))
                curr = curr.next 
        
        heapq.heapify(heap)

        while heap:
            node = heapq.heappop(heap)[2]
            node.next = None
            curr_res.next = node
            curr_res = curr_res.next

        return dummy.next

        