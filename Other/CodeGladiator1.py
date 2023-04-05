''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    v = input()
    b = []
    pos = "POSITIVE"
    neg = "NEGATIVE"
    for i in range (int(input())):
        
        if isSubSeq(v,input()):
            b.append(neg)
        else:
            b.append(pos)
    for _ in b:
        print(_)


def test():
    v= "coronavirus"
    # B= ["abcde","crnas","onarous"]
    B= ["crnas","abcde"]
    i=[]
    pos = "POSITIVE"
    neg = "NEGATIVE"
    for b in B:
        print(b)
        bool = False
        m=0
        n=0
        while( 
            m!= len(v) and n!= len(b)
        ):
            print (v[m:],b[n:])
            if (len(b[n:])==1 and len(v[m:])==1 and v[m:]==b[n:]):
                bool = True
                break

            if (v[m:][0]==b[n:][0]):
                print("equal")
                m+=1
                n+=1
            else:
                print("unequal")
                m+=1
        # bool = isSubSeq(v,i)
        print(bool)
        if bool:
            i.append(pos)
        else:
            i.append(neg)
    print(i)
    for _ in i:
        print(_)

def isSubSeq(v,b):
    
    if (len(b)==1):
        if (len(v)==1):
            if (v==b):
                return True
    elif (len(v)==0 and len(b)!=0):
        return False
    elif (v[0]==b[0]):
        print("equal")
        isSubSeq(v[1:],b[1:])
    elif (v[0]!=b[0]):
        isSubSeq(v[1:],b)
        print("not-equal")
    else:
        print(v,b)
 # Write code here 

# main()
test()

