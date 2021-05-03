if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x=0
    result=0
    while(x<=n):
        if list(student_marks.keys())[x]==query_name:
            avg=list(student_marks.values())[x]
            x=0
            break
        else:
            x+=1
    for x in range (0,len(avg)):
        result+=avg[x]
    result="{0:.2f}".format(result/len(avg))
    print (result)