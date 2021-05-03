def maxSubarrayValue(arr):
    best_sum = 0  
    current_sum = 0
    for i in sub_lists(arr):
        current_sum = findSum(i)
        print(current_sum,best_sum)
        best_sum = max(current_sum,best_sum)
    return best_sum

def findSum(subList):
    evenSum=0
    oddSum=0
    diff =0
    for i in range (0,len(subList)):
        if i%2==0:
            evenSum+=subList[i]
        else:
            oddSum+=subList[i]
    diff = evenSum-oddSum
    return diff*diff

def sub_lists(my_list):
    subs = [[]]
    for i in range(len(my_list)):
        n = i+1
        while n <= len(my_list):
            sub = my_list[i:n]
            if sub not in subs and len(subs) !=0:
                subs.append(sub)
            n += 1
    return subs

print(maxSubarrayValue([1,-1,1,-1,1]))