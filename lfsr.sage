#/usr/bin/env sage

from sage.all import *

def lfsr(init_value, polynomial, field = GF(2)):
    """"
    polynomial can be polynomial in GF with list() -- [c0, c1, ...]
    or a list with corresponding coefficients
    """
    coeffs = list(polynomial)[:-1] # remove the last element
    states = list(init_value)
    assert len(states) == len(coeffs)

    while True:
        feedback = field(0)
        for j, ele in enumerate(coeffs):
            if ele != 0: 
                feedback += states[j]

        states.append(feedback)
        yield states.pop(0)



if __name__ == '__main__':
    seq = [0, 0, 1, 0, 0, 0]
    fun = [1, 0, 0, 0, 1, 1, 1]

    my_lfsr = lfsr(seq, fun)
    for i in range(20):
        print my_lfsr.next(),
    print
