from __future__ import annotations
from typing import Union


class Node:
    def __init__(self, x: int, y: Union[Node, None] = None):
        self.value = x
        self.next = y


class LinkedList:
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

    
    def insert(self, n: int, x: int):
        if n == 0 or not self.top:
            self.top = Node(x, self.top)
        else:
            current_node = self.top
            while current_node.next:
                n -= 1
                if n == 0:
                    break
                current_node = current_node.next
            current_node = Node(x, current_node.next)
            

    def delete(self, n: int):
        if n == 0:
            if self.top:
                self.top = self.top.next
                return True
        else:
            current_node = self.top
            while current_node:
                n -= 1
                if n == 0:
                    current_node = current_node.next
                    return True
                current_node = current_node.next
            return False


l = LinkedList()
l.insert(0, 2)
l.insert(0, 9)
l.insert(0, 7)
l.delete(0)
print(l)
