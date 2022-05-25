#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    node=SinglyLinkedListNode(data)    
    
    if head is None:
        head=node
    else:
        curr_node=head
        while curr_node.next:
            curr_node=curr_node.next
        curr_node.next=node
    return head
    # print(head)
    # while tail.next!=None:
    #     tail=tail.next
    #     print(tail.data,tail.next)
        
if __name__ == '__main__':
