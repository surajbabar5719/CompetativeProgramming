# Enter your code here. Read input from STDIN. Print output to STDOUT

d,m,y=map(int,input().split(' '))
ddue,mdue,ydue=map(int,input().split(' '))
if (y,m,d)<=(ydue,mdue,ddue):
    print(0)
elif (y,m)==(ydue,mdue):
    print((d-ddue)*15)
elif y==ydue:
    print((m-mdue)*500)
else:
    print(10000)

