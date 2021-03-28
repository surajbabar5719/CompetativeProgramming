class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        if head is None or head.next is None:
            return head
        data=[head.data]
        current=head
        while current.next is not None:
           # print(current.data)
            if current.next.data in data:
                current.next=current.next.next
            else:
                data.append(current.next.data)
                current=current.next
        return head
mylist= Solution()
