m = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]


mn = (len(m[0]),len(m))

def r(m):
    left, right = 0,mn[0]-1
    top, bottom = 0, mn[1]-1
    
    while left<right and top < bottom:
        
        prev = m[top+1][left]
        
        for lr in range(left,right+1):
            curr = m[top][lr]
            m[top][lr] = prev
            prev = curr
        top +=1
        
        for tb in range(top,bottom+1):
            curr = m[tb][right]
            m[tb][right] = prev
            prev = curr
        right-=1
        
        for rl in range(right,left-1,-1):
            curr = m[bottom][rl]
            m[bottom][rl] = prev
            prev = curr
        bottom-=1
        
        for bt in range(bottom,top-1,-1):
            curr = m[bt][left]
            m[bt][left] = prev
            prev = curr
        left +=1
    return m

# print(r(m))
for i in r(m):
    print(*i)
        
