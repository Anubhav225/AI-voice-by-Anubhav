class Solution:
    def sortList(self, head):
        values = []
        curr = head

        while curr:
            values.append(curr.val)
            curr = curr.next

        values.sort()

        curr = head
        for value in values:
            curr.val = value
            curr = curr.next

        return head