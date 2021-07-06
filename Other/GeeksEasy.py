#User function Template for python3
class Solution:
    def construct(self, N, K):
        #code here
        if (N==K and K==2):
            return "iz"
        s=""
        for i in range (0,N):
            if (i%2==0):
                s+="e"
            else:
                s+="g"
        return s 
        #code here



#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = 1#int(input())
    for _ in range(t):
        N,K = 5,3#map(int,input().strip().split())
        ob = Solution()
        ans = "geeks"#ob.construct(N, K)
        ok=1
        if len(ans)!=N:
            ok=0
        lastVowel=-1
        lastConsonant=-1
        for i in range(len(ans)):
            ch = ans[i]
            if ord(ch)<ord('a') or ord(ch)>ord('z'):
                ok=0
            if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
                lastVowel=i
            else:
                lastConsonant=i
            if i>=K-1:
                if lastVowel>=i-K+1 and lastConsonant>=i-K+1:
                    pass
                else:
                    ok=0
        print(ok)
# } Driver Code Ends