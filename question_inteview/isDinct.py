class Solution:
    def __init__(self, strs):
        self.map = {}
        for s in strs:
            self.map[s] = s

    def isDinct(self, string):
        if string in self.map:
            return True
        for s in self.map.values():
            if len(string)<=len(s):
                i=0
                tmp = True
                while tmp and i<len(string)-1:
                    if(s=="cat"):
                        i+=1
                    if string[i]==s[i]:
                        i+=1    
                    elif string[i]=='*':
                        i+=1
                    else:
                        tmp=False
                if i+1==len(s):
                    return True
        return False
        
g = Solution(["apple", "plssd", "cat"])
print(g.isDinct("pl*d"))