class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = strs[0]
        for i in range(len(strs)) :
            for j in range(len(common_prefix)) :
                try :
                    if common_prefix[j] == strs[i][j] :
                        continue
                    else :
                        common_prefix=common_prefix[:j]
                except :
                    common_prefix=common_prefix[:j]
        return common_prefix
    
        
                    