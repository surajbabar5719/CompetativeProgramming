'''
https://www.hackerearth.com/problem/algorithm/micro-and-array-1/
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
N,Q=map(int,input().split(' '))
arr=list(map(int,input().split(' ')))
for _ in range(Q):
    que=list(map(int,input().split()))
    if que[0]==0:
        arr[que[1]-1]=que[2]
    else:
        maxval=-1
        for i in range(len(arr)):
            if arr[i]>=que[1]:
                maxval=i+1
                break
        print(maxval)
