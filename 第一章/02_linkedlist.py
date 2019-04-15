# -*- coding: utf-8 -*-
# 如何创建一个链表

class Node(object):
    '''节点'''

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class Singerlinkerlist(object):
    '''单链表'''

    def __init__(self, node=None):
        self._head = node

    def is_empty(self):
        '''判断是否为空'''
        return self._head == None

    def length(self):
        '''求长度'''
        # cur游标，遍历节点
        cur = self._head
        # count计数
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历'''
        # cur游标，遍历节点
        cur = self._head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next

    def append(self, item):
        '''尾部插入节点'''
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self, item):
        '''在链表头部添加元素'''
        node = Node(item)
        node.next = self._head
        self._head = node

    def insert(self, pos, items):
        '''任意位置添加参数
        pos 从零开始
        '''
        pre = self._head
        node = Node(items)
        if pos <= 0:
            self.add(items)
        elif pos > self.length():
            self.append(items)
        else:
            for j in range(pos - 1):
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        '''查找'''
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
        if self.length() == 0:
            print('It is empty')

    def remove(self, item):
        '''删除节点'''
        cur = self._head
        pre = None
        while cur != None:
            if cur.elem == item:
                #先判断是否为头结点
                if cur==self._head:
                    self._head=cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    li = Singerlinkerlist()
    print(li.is_empty())
    print(li.length())
    li.append(1)
    print(li.is_empty())
    print(li.length())
    li.append(2)
    li.append(3)

    li.add(4)
    li.insert(100, 100)
    li.travel()
    li.search(9)
    li.remove(4)
    li.travel()
