from __future__ import annotations
from typing import Union


class Node:
    def __init__(self, x: int, y: Union[Node, None] = None):
        self.value = x
        self.next = y


class LinkedListStack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        elems = '['
        current_node = self.top 
        while current_node:
            if current_node.next is None:
                elems += str(current_node.value) + ']'
            else:
                elems += str(current_node.value) + ', '
            current_node = current_node.next
        return elems

    # 先頭に追加
    def push(self, x: int):
        if not self.top:
            self.top = Node(x, self.top)
        else:
            current_node = self.top
            new_node = Node(x, current_node)
            self.top = new_node

    # 先頭を削除
    def pop(self):
        if self.top:
            self.top = self.top.next

            
class LinkedListQueue:            
    def __init__(self):
        self.top = None
    
    def __str__(self):
        elems = '['
        current_node = self.top 
        while current_node:
            if current_node.next is None:
                elems += str(current_node.value) + ']'
            else:
                elems += str(current_node.value) + ', '
            current_node = current_node.next
        return elems

    # 末尾に追加
    def enqueue(self, x: int):
        if not self.top:
            self.top = Node(x, self.top)
        else:
            current_node = self.top
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(x, current_node.next)

    # 先頭を削除
    def dequeue(self):
        if self.top:
            self.top = self.top.next


st = LinkedListStack()
st.push(8)
st.push(2)
st.push(111)
st.pop()
print(st)

eq = LinkedListQueue()
eq.enqueue(10)
eq.enqueue(20)
eq.enqueue(30)
eq.dequeue()
print(eq)
