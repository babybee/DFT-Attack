#!/usr/bin/env sage

from sage.all import *

# by using the default field might cause some problem
# e.g. computing based on two different fields?
def convolution(sequence, polynomial, field = GF(2)):
    "return a generator of the filtered sequence"
    coeffs = list(polynomial)

    assert len(coeffs) < len(sequence)

    for t in range(len(sequence) - len(coeffs) + 1):
        result = field(0)
        for i, coe in enumerate(coeffs):
            result += coe * sequence[i + t]
        yield result

if __name__ == '__main__':
    seq = (1, 1, 0, 0, 1, 1)
    fun = (1, 1)

    gen = convolution(seq, fun)
    for i in gen:
        print i,
    print
