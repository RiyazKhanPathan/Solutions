# Python code to group anagrams

anagrams = ["cat","tac","bag","gab","act","tell","yell"]
groups={}

def k(key):
    return "".join(sorted(key))
    
for key in anagrams:
    sortedKey = k(key)
    if sortedKey not in groups.keys():
        groups[sortedKey]=[key]
    else:
        groups[sortedKey].append(key)

for key,val in groups.items():
    if len(val)>1:
        print(*val)
    

# ######## OUTPUT ###########
# cat tac act
# bag gab
