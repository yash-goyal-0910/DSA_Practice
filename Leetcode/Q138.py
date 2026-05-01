'''
Question topic - Linked List
Question link - https://leetcode.com/problems/copy-list-with-random-pointer
'''
# Sol - 
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    dic = {}
    if not head:
        return None
    head_t = head
    res = Node(0)
    temp = res
    x = 0
    temp.val = head.val
    head.val = x
    dic[x] = temp
    while head.next:
        x += 1
        head = head.next
        temp.next = Node(0)
        temp = temp.next
        temp.val = head.val
        head.val = x
        dic[x] = temp
    temp = res
    while head_t:
        if head_t.random:
            temp.random = dic[head_t.random.val]
        temp = temp.next
        head_t = head_t.next
    return res