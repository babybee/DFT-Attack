#!/usr/bin/env sage

from sage.all import *

import defs

#TheFiniteField = GF(2)
#ThePolynomialRing = TheFiniteField['X']

def bma(s):    
    "using the notations in 'Shift-register synthesis and BCH decoding' by Massey"
    C = defs.ThePolynomialRing(1)
    B = defs.ThePolynomialRing(1)

    b = defs.TheFiniteField(1)

    m = 1 # replacing the orignial notation, x
    L = 0

    for N in range(len(s)):
        d = defs.TheFiniteField(s[N])
        for l in range(1, len(C.list())): # range(1, L + 1) will cause out-of-index error
            d += C.list()[l] * defs.TheFiniteField(s[N - l])

        if d == 0:
            m += 1
        else:
            if 2 * L > N:
                C -= d / b * B.shift(m)
                m += 1
            else:
                T = C
                C -= d / b * B.shift(m)
                L = N + 1 - L
                B = T
                b = d
                m = 1

    C = C.reverse()
    # must be reversed in this notation
    return C.shift(L - C.degree())
    # because reverse() cannot guarantee the overall degree
    # so this is the very reason why the original BMA always output $L$!!!

if __name__ == '__main__':
    seq = (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0)
    #seq = (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0)
    pol = bma(seq)
    
    print 'The input sequence is', seq
    print 'Its characteristic polynomial is', pol
