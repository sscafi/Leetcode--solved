class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0 :
            return 0
        elif n == 1 :
            return 1
        elif  n == 2 :
            return 2
        else :
            onestep = 1
            twostep = 2

        for i in range(3 , n + 1):
            current = twostep + onestep
            onestep = twostep
            twostep = current
        
        return current
