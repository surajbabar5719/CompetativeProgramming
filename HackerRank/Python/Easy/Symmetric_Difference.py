# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    input()
    a=set(map(int,input().split(' ')))
    input()
    b=set(map(int,input().split(' ')))
    ans=sorted(list(a-b | b-a))
    print(*ans,sep='\n')
