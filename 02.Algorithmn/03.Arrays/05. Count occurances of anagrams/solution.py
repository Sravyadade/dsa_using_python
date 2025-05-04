MAX = 256

class Solution:
    def compare(self, count, countW):
        for i in range(MAX):
            if count[i] != countW[i]:
                return False
        return True

    def search(self, pat, txt):
        M = len(pat)
        N = len(txt)
        count = [0] * MAX
        countW = [0] * MAX
        
        for i in range(M):
            countW[ord(pat[i])] += 1
            count[ord(txt[i])] += 1
        
        x = 0
        for i in range(M, N):
            if self.compare(count, countW):
                x += 1
            
            count[ord(txt[i])] += 1
            count[ord(txt[i - M])] -= 1
        
        if self.compare(count, countW):
            x += 1
        
        return x

# Driver code
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        txt = input()
        pat = input()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
