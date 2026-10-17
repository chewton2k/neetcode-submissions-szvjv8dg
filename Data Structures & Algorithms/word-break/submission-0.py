class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n + 1)    
        dp[0] = True

        for i in range(n): 
            
            if not dp[i]: 
                continue 

            for word in wordDict: 
                end = i + len(word)

                if end <= n and s[i:end] == word:
                    dp[end] = True


        return dp[n]
