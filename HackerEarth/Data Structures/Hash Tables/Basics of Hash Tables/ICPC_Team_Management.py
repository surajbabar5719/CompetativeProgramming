'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def count(arr,k):
    for i in set(arr):
        if arr.count(i)%k != 0:
            return False
    return True
if __name__=='__main__':
    for _ in range(int(input())):
        n,k=map(int,input().split(' '))
        arr=[]
        for _ in range(n):
            arr.append(len(input()))
        if count(arr,k):
            print('Possible')
        else:
            print('Not possible')
