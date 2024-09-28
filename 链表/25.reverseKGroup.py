# 链表中每k个元素翻转
# 思路： 
# 1. 翻转长度为k的链表
# 2. 将翻转后的链表接到原来的链表上，注意使用一个dummynode来指向最终的头结点，会更方便处理

class Solution:
    def reverseKGroup(self, head, k):
        dummyHead = ListNode(0, head)
        pre = dummyHead
        tail = pre
        while head:
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummyHead.next
            nextNode = tail.next
            # 翻转0-k的链表
            head, tail = self.reverse(head, tail)
            # 将翻转链表接入原来的链表中，pre指向head，tail指向nextNode
            # 更新pre，head，继续循环
            pre.next = head
            tail.next = nextNode
            pre = tail #pre记录上一个翻转链表的尾结点
            head = tail.next
        return dummyHead.next


    def reverse(self, head, tail):
        pre = tail.next #pre首先记录尾结点的下一个节点，是下一个链表的头结点，翻转链表K之后的尾结点指向下一个链表的头结点
        cur = head
        while pre != tail:
            temp = cur.next
            cur.next = pre
            cur = temp
            pre = cur
        return tail, head #翻转链表后，原来的尾结点是头结点，原来的头结点变成尾结点