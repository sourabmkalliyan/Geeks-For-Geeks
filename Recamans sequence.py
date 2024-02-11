# Recamans sequence - Geeks for Geeks


class Solution:
    def recamanSequence(self, n):
        ans = [0,1]
        visited = {0, 1}
        current = 1
        if n < 2:
            return ans
        for i in range(2, n+1):
            if current - i >= 0 and current - i not in visited:
                current = current - i
            else:
                current = current + i
            visited.add(current)
            ans.append(current)
        return ans