#User function Template for python3
class Solution:
    def fun(self,k):
        if k in [0,1,2]:
            return k
        if k%2==0:
            return Solution().fun(k//2)
        else:
            return Solution().fun((k-1)//2)

    def geekPair(self, Arr, N):
        dynamic = {}
        sol = Solution()
        for i in Arr:
            print(i)
            print(sol.fun(i))
        # code here
    

        

        
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        
        ob = Solution()
        print(ob.geekPair(Arr, N))
# } Driver Code Ends