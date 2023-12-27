class Solution(object):
    def lengthOfLastWord(self, s):
        j,i=0,0
        cnt=0
        while i<len(s):
            tmp=False
            if(s[i]!=' '):
                cnt=0
                while i<len(s) and s[i]!=' ':
                    cnt+=1
                    i+=1
                    tmp=True
                print(cnt)
            if tmp==False:
                i+=1
            
        return cnt