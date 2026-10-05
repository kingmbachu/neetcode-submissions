class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1. Create a dummy node pointing to the head to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        # 2. Advance the fast pointer n + 1 steps to create the proper gap
        for _ in range(n + 1):
            fast = fast.next
            
        # 3. Move both pointers together until fast reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next
            
        # 4. slow is now right before the target node; skip the target node
        slow.next = slow.next.next
        
        # Return the actual head of the modified list
        return dummy.next