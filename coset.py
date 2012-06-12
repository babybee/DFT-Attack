#!/usr/bin/env python

def coset(N):
    "return a dict with coset leaders and its cosets size"
    result = {}

    # N must be odd
    assert N % 2 == 1

    flag = [False] * N
    for x in range(N):
        if flag[x]: # if already processed
            continue

        size = 1
        while (x * (2 ** size)) % N != x:
            flag[(x * (2 ** size)) % N] = True
            size += 1

        result[x] = size

    return result


if __name__ == '__main__':
    for i in range(1, 100, 2):
        print i, coset(i)
