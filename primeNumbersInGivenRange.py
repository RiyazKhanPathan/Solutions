def isPrime(n):
    i = 2;
    while(i<n):
        if n%i == 0:
            return False;
        i+=1
    return True;

def data(n,rangee):
    if(n==rangee and isPrime(n)):
        print(n)
    while(True):
        if isPrime(n):
            print(n)
       
        if(n<=rangee):
            n += 1
            if(n>rangee):
                break
        else:
            n -= 1
            if(n<rangee):
                break
   
li = list(map(int,input().split()))

data(li[0],li[1])
