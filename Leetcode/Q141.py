'''
Question topic - Linked List
Question link - https://leetcode.com/problems/linked-list-cycle
'''
# Sol - 
def hasCycle(head: Optional[ListNode]) -> bool: 
    N1 = head
    if not N1:
        return False
    N2 = head.next
    if not N2:
        return False
    while N2 and N2.next:
        if N1 == N2:
            return True
        else:
            N1 = N1.next
            N2 = N2.next.next
    return False