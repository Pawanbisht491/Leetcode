class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        ans = ListNode(0)
        curr3 = ans
        c = 0
        while curr1 or curr2:
            total = c
            c = 0
            if curr1:
                total += curr1.val
                curr1 = curr1.next
            if curr2:
                total += curr2.val
                curr2 = curr2.next
            if total > 9:
                c = 1
                total -= 10
            new_Node = ListNode(total)
            curr3.next = new_Node
            curr3 = curr3.next
        if c > 0:
            newNode = ListNode(c)
            curr3.next = newNode
        return ans.next