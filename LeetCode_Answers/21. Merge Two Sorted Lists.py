# Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

# Rules:
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for a singly-linked list node.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val  # The value of the node
        self.next = next  # Pointer to the next node in the list

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merges two sorted linked lists into one sorted linked list.
        """
        # Create a dummy node to serve as the starting point of the merged list.
        # This helps avoid special cases when adding the first element.
        randomListNode = ListNode()

        # Tail will always point to the last node of the merged list.
        tail = randomListNode

        # Loop as long as both lists are not empty
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                # If list1's value is smaller, attach it to the merged list
                tail.next = list1

                # Move list1 to the next node
                list1 = list1.next
            else:
                # If list2's value is smaller or equal, attach it to the merged list
                tail.next = list2

                # Move list2 to the next node
                list2 = list2.next

                # Move the tail forward to the newly added node
            tail = tail.next

            # At this point, one of the lists is empty.
        # Attach the remaining part of the non-empty list to the merged list.
        if list1 is not None:
            tail.next = list1  # If list1 is not empty, attach it.
        elif list2 is not None:
            tail.next = list2  # If list2 is not empty, attach it.

        # Return the head of the merged list, which is next to the randomListNode node
        return randomListNode.next

# Analysis:
# The complexity of this solution is O(n + m), where n and m are the lengths of list1 and list2, respectively. We
# traverse, in the worst case, through all the nodes of both lists. The space complexity is O(1) since we only use a
# constant amount of space.
