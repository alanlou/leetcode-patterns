# O(M * 2^N * 2^N)
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        
        # construct valid_seats array
        valid_seats = [0] * m
        for i in range(m):
            for j in range(n):
                valid_seats[i] |= (1 << j) if seats[i][j] == "." else 0
        
        def bit_count(n):
            cnt = 0
            while n:
                n &= n - 1 
                cnt += 1
            return cnt
        
        @cache
        def dp(idx, prev_mask):
            if idx == m:
                return 0
            
            ans = 0
            for mask in range(1 << n):
                if (mask & valid_seats[idx] == mask) and (mask & (mask << 1) == 0) and\
                (prev_mask & (mask << 1) == 0) and (prev_mask & (mask >> 1) == 0):
                    ans = max(ans, bit_count(mask) + dp(idx + 1, mask))
            return ans
        
        return dp(0, 0)