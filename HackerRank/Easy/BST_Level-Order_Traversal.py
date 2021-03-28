import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def height(self,root):
        if root is None:
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        return max(lheight,rheight) + 1
    def printLevelOrder(self,root,level):
        if root is None:
            return 0
        if level is 0:
            print(root.data,end=' ')
        else:
            self.printLevelOrder(root.left,level-1)
            self.printLevelOrder(root.right,level-1)
    def levelOrder(self,root):
        #Write your code here
        d=self.height(root)
        for i in range(d+1):
            self.printLevelOrder(root,i)
        

T=int(input())
