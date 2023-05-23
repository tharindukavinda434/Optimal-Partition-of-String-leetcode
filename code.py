class Solution(object):
    def partitionString(self, s):
        L=[]
        i=0
        while(i<len(s)):
            K =[]
            while(s[i] not in K):
                K.append(s[i])
                i=i+1
                if (i>= len(s)):
                    break


            L.append(K)
        return(len(L))
