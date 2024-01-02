

def FirstCharNotRep(str):
    hashmap={}
    for c in str:
        hashmap[c]=1+hashmap.get(c,0)
    for c in str:
        if hashmap[c]==1:
            return c
    print(hashmap)

print(FirstCharNotRep('abacabad'))