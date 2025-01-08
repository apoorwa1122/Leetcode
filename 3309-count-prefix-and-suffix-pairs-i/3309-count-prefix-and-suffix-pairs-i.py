class Solution(object):
    def countPrefixSuffixPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def isPrefixAndSuffix(str1, str2):
            if (str2.startswith(str1) and str2.endswith(str1) ):
                return True            
            return False
    

        n=len(words)
        cnt=0        
        for i in range(n):
            for j in range(i+1, n):
                if(isPrefixAndSuffix(words[i], words[j])):
                    cnt+=1
                            

        return cnt     