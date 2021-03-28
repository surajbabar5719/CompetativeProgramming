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
    def getHeight(self,root):
        ans=self.maxHeight(root)
        return ans-1
    def maxHeight(self,root):
        #Write your code here
        if root == None:
            return 0
        #print(root.data)
        ldepth=self.maxHeight(root.left)
        rdepth=self.maxHeight(root.right)
        #print(root.data,ldepth,rdepth)
        return max((rdepth,ldepth))+1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
