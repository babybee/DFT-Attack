#!/usr/bin/env sage

from sage.all import *

from bma import bma
from lfsr import lfsr
from coset import coset


def dft(sequence):
    N = len(sequence)
    fun_p = bma(sequence)
    L = fun_p.degree()
    assert 2 * L <= N
    # should have some backup procedure?

    # selection of parameters
    # fine smallest n
    n = 1
    while 0 == (2 ** n - 1) % n:
        n += 1

    # define the extension field
    TheExtensionField = GF(2 ** n, 'beta')
    beta = TheExtensionField.gen()
    fun_f = TheExtensionField.polynomial()

    # construct a new m-seq {b_t}
    seq_b_iv = []
    for i in range(n):
        seq_b_iv.append((beta ** i).trace())
    seq_b_generator = lfsr(fun_f, seq_b_iv)

    # let alpha be an element in GF(2^n) with order N
    alpha = beta ** ((2 ** n - 1) / N)

    # procedure
    # step 1. compute coset
    I = coset(N)

    # step 2. 
    fun_p_extended = TheExtensionField(fun_p)

    spectra_A = {}
    for k in I:
        if fun_p_extended(alpha ** k) != 0:
            spectra_A[k] = 0
            continue

        # sub-routine for computing A_k
        # 1. get coset size
        m = I[k]









    
    

    print type(seq_b_iv[0])

    for i in seq_b:
        print i,
    print 


    return n



if __name__ == '__main__':
    print dft([1, 1, 1, 1, 0, 0, 1, 1, 1])
