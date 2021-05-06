#!/usr/bin/python
# -*- coding: utf-8 -*-


def count(S, n, N):
    incl = count(S, n, N - S[n])
    excl = count(S, n - 1, N)
    return incl + excl


if __name__ == '__main__':
    c = int(input())
    S = []
    for i in range(c):
        S.append(int(input()))
    N = int(input())

    print(count(S, len(S) - 1, N))
