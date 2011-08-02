#!/usr/bin/env sage

from bma import bma

def dft(sequence):
    N = len(sequence)
    px = bma(sequence)
    L = px.degree()
    assert 2 * L <= N
    # should have some backup procedure?

    # fine smallest n
    n = 1
    while 0 == (2**n - 1) % n:
        n += 1



    return n



if __name__ == '__main__':
    print dft([1, 1, 1, 1, 0, 0, 1, 1, 1])
