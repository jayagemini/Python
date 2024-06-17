from ListNode import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(0)
        cur=dummy
        carry=0

        while l1 or l2 or carry!=0:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            val=v1 + v2 +carry

            carry=val//10
            val=val%10

            cur.next=ListNode(val)
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return  dummy.next






        
