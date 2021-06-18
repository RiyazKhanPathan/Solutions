def isPrime(n):
    i=2;
    while(i<n):
        if n % i==0 and i!=n:
            return False;
        i+=1
    return True;

def nearestPrime(n):
    k=n
    while(True):
        if isPrime(n):
            return n
        elif isPrime(k):
            return k
     return "Number should be >=2"
        n+=1 #positive check
        k-=1 #negative check
    
