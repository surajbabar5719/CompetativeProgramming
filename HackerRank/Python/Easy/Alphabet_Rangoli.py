def print_rangoli(size):
    # your code goes here
    arr=[chr(i) for i in range(97,97+size)]
    arr=arr[:0:-1]+arr
    #print(arr)
    array=[]
    for i in range(size):
        #print(arr)
        array.append('-'.join(arr))
        try:
            arr.pop(size)
            arr.pop(size-1)
            arr.insert(0,'-')
            arr.append('-')
        except:
            pass
    array=array[:0:-1]+array
    print(*array,sep='\n')
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
