# O(H * N * 2^N) / O(H * 2^N)
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        
        n, MOD = len(hats), 10 ** 9 + 7
        
        # construct hat to people dict
        h2p = collections.defaultdict(list)
        for p, hs in enumerate(hats):
            for h in hs:
                h2p[h].append(p)
        
        full_mask = (1 << n) - 1
        
        @cache
        def dp(i, mask):
            # base case: everyone has hat
            if mask == full_mask:
                return 1
            
            # base case: run out of hats
            if i == 41:
                return 0
            
            # case 1. skip current hat
            ans = dp(i + 1, mask)
            
            # case 2. take current hat
            for p in h2p[i]:
                # this person already has hat
                if mask & (1 << p):
                    continue
                # let person p take current hat
                ans = (ans + dp(i + 1, mask | (1 << p))) % MOD
            
            return ans
        
        return dp(0, 0)
    