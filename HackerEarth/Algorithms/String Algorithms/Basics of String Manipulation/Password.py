'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def do():
    lst=[]
    for _ in range(int(input())):
        pwd=input()
        if pwd[::-1] in lst:
           # print(pwd)
            print(len(pwd),pwd[len(pwd)//2])
            break
        else:
            lst.append(pwd)
# Write your code here
if __name__ == '__main__':
    do()
