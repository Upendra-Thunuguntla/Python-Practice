#User function Template for python3
class Solution:
    def minimumReduction(self, N, edges, S):
        #code here
        print(edges)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Edge:
    def __init__(self):
        self.u = None
        self.v = None
        self.w = None
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        N,S=map(int,input().split())
        edges = [Edge() for i in range(N - 1)]
        for i in range(N - 1):
            edges[i].u, edges[i].v, edges[i].w = map(int, input().split())
        ob = Solution()
        print(ob.minimumReduction(N, edges, S))
# } Driver Code Ends