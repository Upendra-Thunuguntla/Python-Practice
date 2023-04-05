def findMin(deno, V):
    n = len(deno)
    ans = []
    i = n - 1
    while i >= 0:
        while V >= deno[i]:
            V -= deno[i]
            ans.append(deno[i])
        i -= 1
    return len(ans)

if __name__ == '__main__':
    c = int(input())
    inputArr = []
    for i in range(c):
        inputArr.append(int(input()))
    total = int(input())
    print (findMin(inputArr, total))
