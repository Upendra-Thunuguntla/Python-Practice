n=input()
for x in range (0,5):
    try: 
        i= input()
        a= int(i[0])
        b= int(i[2])
        print (a//b)
    except ValueError as e:
        print ("Error Code:",e)
    except ZeroDivisionError as e:
        print ("Error Code:",e)