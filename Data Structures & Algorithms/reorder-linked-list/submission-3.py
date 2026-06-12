# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 切一半找中點(龜兔賽跑)
        if not head or not head.next:
            return

        fast = head.next.next
        slow = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next # 中點
        slow.next = None

        # 後半段反轉
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #prev 會變成反轉後的頭

        # 交錯合併
        first = head
        second = prev
        #[0, 1, 2, 3]
        #[6, 5, 4]
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2