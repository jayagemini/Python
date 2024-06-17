class Solution(object):
    def longestCommonPrefix(self, strs):
        commonprefix=""
        for i in range(len(strs[0])):
            for j in strs:
                if i==len(j) or j[i]!=strs[0][i]:
                    return commonprefix
                
            commonprefix=commonprefix+strs[0][i]

        
        return commonprefix           



        
c=Solution()
print(c.longestCommonPrefix(["ab", "a"])) 
#print(c.longestCommonPrefix(["dog","racecar","car"])) 

