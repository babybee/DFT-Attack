#!/usr/bin/env sage

from sage.all import *

# by using the default field might cause some problem
# e.g. computing based on two different fields?
def convolution(sequence, polynomial, field = GF(2)):
    "return a generator of the filtered sequence"
    coeffs = list(polynomial)
    period = len(sequence) # so must be a full period or do not use the whole sequence

    t = 0
    while True:
        result = field(0)
        for i, coe in enumerate(coeffs):
            result += coe * sequence[(i + t) % period]
        t += 1
        yield result

if __name__ == '__main__':
    seq = (1, 1, 0, 0, 1, 1)
    fun = (1, 1)

    gen = convolution(seq, fun)
    for i in range(20):
        print gen.next(),
    print
