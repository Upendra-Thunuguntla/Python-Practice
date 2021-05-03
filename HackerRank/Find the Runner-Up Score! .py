if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    win=max(arr)
    while (win==max(arr)):
        arr.remove(max(arr))
    print(max(arr))


            