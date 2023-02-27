'''
n(n+1)/2 = bricks
(n**2)+n = 2*bricks
(n**2)+n+(1/2)**2 = 2*bricks+(1/4)
(n+(1/2))**2 = 2*bricks+(1/4)
n = sqrt(2*bricks+0.25) - 0.5
'''

def get_complete_steps(n):
    from math import floor, sqrt
    return floor(sqrt(2*n+0.25)-0.5)

T = 1218
print(get_complete_steps(T)) # 48
