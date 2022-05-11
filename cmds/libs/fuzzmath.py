import math

class Calculator():
    def P(self , n , r):
        ans = 1
        for i in range(n-r+1,n+1):
            ans *= i

        return ans