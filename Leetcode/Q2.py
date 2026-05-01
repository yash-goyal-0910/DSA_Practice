'''
Question topic - Linked List
Question link - https://leetcode.com/problems/add-two-numbers
'''
# Sol - 
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    head = l1
    p_l1 = l1
    p_l2 = l2
    while l1 and l2:
        v = l1.val + l2.val + carry
        carry = v // 10
        v = v % 10
        l1.val = v
        p_l1 = l1
        p_l2 = l2
        l1 = l1.next
        l2 = l2.next
    while l1:
        v = l1.val + carry
        carry = v // 10
        v = v % 10
        l1.val = v
        p_l1 = l1
        l1 = l1.next
    while l2:
        v = l2.val + carry
        carry = v // 10
        v = v % 10
        p_l1.next = ListNode()
        p_l1.next.val = v
        p_l1 = p_l1.next
        l2 = l2.next
    if carry:
        p_l1.next = ListNode()
        p_l1.next.val = 1
    return head