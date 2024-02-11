# Geeks for Geeks - Problem of the Day
# Decmeber 16, 2023
# Strings Count

class Solution:

    def countStr(self, n):
       ans = (1 + 2*n) + (n*(n*n - 1)//2)
       return ans

