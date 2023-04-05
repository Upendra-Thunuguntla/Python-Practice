class Solution:
    def jump(self, nums):
        count,size = 0,len(nums)
        if size==1:
            return 0
        op = []
        flag = True
        for x in range (size-1):
            
            count = x
            if nums[x]==size:
                return count+1
            y=x
            while (y<size):
                if nums[y]==0:
                    flag = False
                    break
                y += nums[y]
                count+=1
            
            if flag:
                if y>size:
                    op.append(count)
                else:
                    op.append(count-1)
            flag = True
        return min(op)

print(Solution().jump([1,2,3]))