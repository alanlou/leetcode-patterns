# O(N * 2^M)
class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        m, n = len(req_skills), len(people)
        mapping = {v: i for i, v in enumerate(req_skills)}
        
        # convert each person's skills into bitmask
        skill_masks = [0] * n
        for i, p in enumerate(people):
            for skill in p:
                if skill in mapping:
                    skill_masks[i] |= (1 << mapping[skill])
        
        full_mask = (1 << m) - 1
        
        @cache
        def dp(mask):
            if mask == full_mask:
                return []
                
            ans = [0] * (n + 1)
            for i, skill_mask in enumerate(skill_masks):
                nxt_mask = mask | skill_mask
                if mask != nxt_mask:
                    ans = min(ans, [i] + dp(nxt_mask), key=len)
            return ans
        
        return dp(0)