# -*- coding: utf-8 -*-
'''双向链表'''


class Node(object):
    '''定义节点'''

    def __init__(self, elem):
        self.elem = elem
        self.prev = None
        self.next = None


class Dllist(object):
    '''实现双向链表'''

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        '''判断是否为空'''
        return self.__head is None

    def length(self):
        '''求长度'''
        count = 0
        cur = self.__head
        if self.__head is not None:
            count = count + 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历'''
        cur = self.__head
        while self.__head is not Node:
            print(cur.elem, ' ')
            cur = cur.next

    def predend(self, elem):
        '''头部插入节点'''
        node = Node(elem)
        node.next_ = self.__head
        # self.__head=node
        # node.next.prev=node
        self.__head.prev = node
        self.__head = node

    def append(self, elem):
        '''尾部增加节点'''
        node = Node(elem)
        if self.is_empty():
            self.predend()
        else:
            cur = self.__head
            if cur.next is not None:
                cur = cur.next
            cur.next=node
            node.prev=cur

    def insert(self,elem,pos):
        '''从任意位置插入节点
            pos从零开始
        '''
        pre=self.__head
        node=Node(elem)
        if pos<=0:
            self.predend(elem)
        elif pos>=self.length():
            self.append(elem)
        else:
            for j in range(pos-1):
                pre=pre.next
            node.prev=pre
            node.next=pre.next
            pre.next=node
            pre.next.prev=node


if __name__ == "__main__":
    dllist = Dllist()
    print(dllist.is_empty())
    print(dllist.length())
    dllist.predend(1)
    print(dllist.is_empty())
    print(dllist.length())
