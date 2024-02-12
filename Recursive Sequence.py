#Recursive Sequence - Geeks for Geeks POTD

class Solution:
    def sequence(self, n):
        ans = 0
        t = 1
        for i in range(1, n+1):
            m = 1
            for j in range(i):
                m = (m*t)%((10**9)+7)
                t += 1
            ans = (ans+m)%((10**9)+7)
        return ans