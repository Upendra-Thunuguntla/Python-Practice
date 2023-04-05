#User function Template for python3
import math
class Solution:
    def makeItOne(self, N):
        count =0
        while(N!=1):
            if (N and (not(N & (N - 1)))):
                N=N//2
                
            else:
                p = int(math.log(N, 2))
                N-= int(pow(2, p))
                
            count+=1
        return count



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        obj = Solution()
        print(obj.makeItOne(N))
# } Driver Code Ends