"""
Explanation:

Decode given string into sections where new section is denoted by single "#"

eg: # ## ### # ## ## #

1
1.1
1.1.1
2
2.1
2.2
3

"""

str = "# ## ## # ## ## ### # ## ### ### ### ### ### ### ### ### ### ### ### ## ### #"

cur=1
prev=""
temp=""
j=0
for i in str.split(" "):
    if(i=="#"):
        temp=f'{cur}'
        j=1
        cur+=1
    elif prev!="#":
        if prev == i:
            temp=temp.replace(f".{j}","")
        elif len(i)>len(prev):
            j=0
        else:
            import re
            temp=re.sub("\..*","",temp)
        j+=1
        temp+=f'.{j}'
  
    else:
        temp+=f'.{j}'
        
    print(temp)
    prev=i

"""
Expected Output

1
1.1
1.2
2
2.1
2.2
2.2.1
3
3.1
3.1.1
3.2
3.3
3.4
3.5
3.6
3.7
3.8
3.9
3.10
3.11
3.12
3.12.1
4

"""
