import re
def main():

 # Write code here
    s = "The use of cubic containers instead of cylindrical ones has proved to be helpful when transporting the substance. Each of the cube can carry 10Kg and has a volume of 1.2 cubic foot."#input()
    c1 = '(\d+(?:\.\d+)?)+\s?groups'
    c2 = '(\d+(?:\.\d+)?)+\s?students'
    c3 = '(\d+(?:\.\d+)?)+\s?people'
    c4 = '(\d+(?:\.\d+)?)+\s?images'
    c5 = '(\d+(?:\.\d+)?)+\s?cubes'

    r1 = '(\d+(?:\.\d+)?)+\s?pixels'
    r2 = '(\d+(?:\.\d+)?)+\s?fl. oz.'
    r3 = '(\d+(?:\.\d+)?)+\s+?mmol/L'
    r4 = '(\d+(?:\.\d+)?)+\s?km'
    r7 = '(\d+(?:\.\d+)?)+\s?metres'
    r6 = '(\d+(?:\.\d+)?)+\s?cubic foot'
    r5 = '(\d+(?:\.\d+)?)+\s?Kg'
    l1 = [c1,c2,c3,c4,c5]
    l2 = [r1,r2,r3,r4,r5,r6,r7]
    l=[];d={}
    for i in l1:
        a = re.search(i,s, re.IGNORECASE)
        if a!=None:
            l.append([a[0],a.span()[0],a.span()[1],'Counts'])
            d[a.span()[0]] = [a[0],a.span()[0],a.span()[1],'Counts']
    for i in l2:
        b = re.search(i,s, re.IGNORECASE)
        if b!=None:
            l.append([b[0],b.span()[0],b.span()[1],'Unit of Measure'])
            d[b.span()[0]] = [b[0],b.span()[0],b.span()[1],'Unit of Measure']
    if len(l)==0:
     print('NONE')
    elif len(l)==1:
     print(l[0][0]+',['+str(l[0][1])+','+str(l[0][2])+'],'+l[0][3], end='\n')
    else:
        dic = sorted(d.items())
        # print(l[0][1],l[1][1])
        for i in dic:
            print(i[1][0]+',['+str(i[1][1])+','+str(i[1][2])+'],'+i[1][3], end='\n')

main()