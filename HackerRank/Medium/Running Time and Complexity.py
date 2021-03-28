# Enter your code here. Read input from STDIN. Print output to STDOUT
def isPrime(n):
   # print(n)
    i=2
    if n==1:
        return False
    while i**2<=n:
        if n%i==0:
            return False
        i+=1
    
    return True
if __name__ == '__main__':
    for _ in range(int(input())):
        n=int(input())
        if isPrime(n):
            print('Prime')
        else:
            print('Not prime')
