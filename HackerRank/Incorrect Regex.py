import re
for x in range(int(input())):
    try:
        re.compile(input())
        print (True)
    except re.error:
        print (False)