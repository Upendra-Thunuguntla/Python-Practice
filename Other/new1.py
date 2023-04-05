def printZ(string,length,height):
    if (height == 1):
        print(string[0])
        return
    else:
        mid = height-2
        j=0
        #Head
        for i in range (height):
            if (j==length):
                j=0
            print(string[j],end =' ')
            j+=1
        print()
        #Body
        cols = mid
        for i in range (mid):
            if (j==length):
                j=0
            for x in range (height):
                if (x==cols):
                    print(string[j])
                    j+=1
                    cols-=1
                    break
                else:
                    print(' ',end=' ')
        #Tail
        for i in range (height):
            if (j==length):
                j=0
            print(string[j],end =' ')
            j+=1
        print()

if __name__ == '__main__':
    total = int(input())
    for i in range (total):
        a, b = map(int, input().split(' '))
        string = input()
        printZ(string,a,b)