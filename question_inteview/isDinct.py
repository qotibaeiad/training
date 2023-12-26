class Solution:
    def __init__(self, strs):
        self.list = strs

    def isDinct(self, string):
        for s in self.list:
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
print(g.isDinct("pl*sd"))
