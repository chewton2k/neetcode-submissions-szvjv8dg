class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: 
            return True
        
        l = r = 0

        while r < len(t) and l < len(s): 
            if s[l] == t[r]: 
                l += 1
                r += 1
            else: 
                r+= 1

            
        if l == len(s): 
            return True


        return False