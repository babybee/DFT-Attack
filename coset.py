#!/usr/bin/env python

def coset(N):
    "return a dict with coset leaders and its cosets size"
    result = dict()

    flags = [False] * N
    for x in range(N):
        if flags[x]: # if already processed
            continue

        size = 1
        while x
