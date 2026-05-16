# Objective: Remove Nth Node From End of Linked List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # Defining a new local variable with a dummy node attached to the
        # beginning of the original linked list.
        dummy = ListNode(0, head)

        # Definining two pointers to traverse the linked list.
        fast = dummy
        slow = dummy

        for _ in range(n):
            # Offsetting the fast pointer to be n steps ahead of the slow pointer.
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        # When the fast pointer has reached the end of the linked list,
        # the next node from the slow pointer's current location
        # is dereferenced.
        slow.next = slow.next.next

        return dummy.next


solution_inst = Solution()

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

answer = solution_inst.removeNthFromEnd(node1, 2)

current = answer

elements = []

while current:
    elements.append(str(current.val))
    current = current.next

print(" -> ".join(elements))
