class Solution:
    def numDecodings(self, s: str) -> int:
        # dp sol'n
        dp = { len(s) : 1 }

        # let's go backwards
        for i in range(len(s) -1, -1, -1):
            # instead of recursively going through values, we cache our results in a map
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and (s[i] == "1" or
                (s[i] == "2" and s[i + 1] in "0123456"))):
                dp[i] += dp[i + 2]
            
        return dp[0]