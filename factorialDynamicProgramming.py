default = {0:1,1:1,2:2}

def f(n):
    if n in default.keys():
        return default[n]
    return n*f(n-1)
    

for i in range(0,10):
    default[i]=f(i)
    
print(default)
