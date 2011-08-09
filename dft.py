#!/usr/bin/env sage

from sage.all import *

from bma import bma
from lfsr import lfsr
from coset import coset
from convolution import convolution
from trace import trace


def dft(seq_a):
    N = len(seq_a)
    fun_p = bma(seq_a * 2) # change the input sequence as periodic
    L = fun_p.degree()
    # print fun_p
    # print L

    # treat the input seq as peroidic so remove this
    # assert 2 * L <= N

    # selection of parameters
    # fine smallest n, s.t. N | (2^n - 1)
    n = 1
    while 0 != (2 ** n - 1) % N:
        n += 1
    # print n

    # define the extension field
    TheExtensionField = GF(2 ** n, 'beta')
    beta = TheExtensionField.gen()
    fun_f = TheExtensionField.polynomial()
    TheExtensionPolynomialRing = TheExtensionField['Y']
    # print fun_f

    # construct a new m-seq {b_t}
    seq_b_iv = []
    for i in range(n):
        seq_b_iv.append((beta ** i).trace())
    seq_b_generator = lfsr(seq_b_iv, fun_f)
    seq_b = []
    for i in range(2 ** len(seq_b_iv) - 1):
        seq_b.append(seq_b_generator.next())
    # print seq_b_iv
    # print seq_b

    # let alpha be an element in GF(2^n) with order N
    alpha = beta ** ((2 ** n - 1) / N)
    # print alpha, alpha ** N

    # procedure
    # step 1. compute coset
    I = coset(N)
    # print I

    # step 2. 
    fun_p_extended = TheExtensionPolynomialRing(fun_p)
    # print fun_p_extended

    spectra_A = [None] * N
    for k in I:
        if fun_p_extended(alpha ** k) != 0:
            spectra_A[k] = 0
            continue

        # print 'k', k, fun_p_extended(alpha ** k)

        # sub-routine for computing A_k
        # 1. get coset size
        m = I[k]
        # print k, m, n

        # 2. k-decimation sequence
        seq_c = []
        if m == n:
            for t in range(2 * m):
                seq_c.append(seq_b[(t * k) % (2**n - 1)])
        elif m < n:
            for t in range(2 * m):
                seq_c.append(trace(alpha ** (k * t), m))
        else:
            import sys
            sys.stderr.write("should never happen?\n")
            sys.exit(-1)

        # print seq_b
        # print seq_c

        fun_p_k = bma(seq_c)
        # print fun_p
        # print fun_p_k
        # print fun_p / fun_p_k

        matrix_M_ele = []
        for i in range(m):
            for ele in range(i, m + i):
                matrix_M_ele.append(seq_c[ele])
        matrix_M = matrix(GF(2), m, m, matrix_M_ele)
        # print matrix_M

        # 3. contruct a filter
        fun_q = fun_p.parent()(fun_p / fun_p_k)
        # print fun_q
        # print type(fun_q)

        # 4. compute the time convolution
        seq_v_generator = convolution(seq_a, fun_q)
        seq_v = []
        for i in range(m):
            seq_v.append(seq_v_generator.next())

        # 4.5 solve linear equations to get x_i
        matrix_x = matrix_M.inverse() * matrix(GF(2), m, 1, seq_v)

        # 5. compute A_k = V * T
        V = 0
        for i in range(m):
            if 1 == matrix_x[i][0]:
                V += alpha ** (i * k)

        fun_q_extended = TheExtensionPolynomialRing(fun_q)
        # print fun_q_extended
        T = fun_q_extended(alpha ** k) ** (-1)
        # print T
        # print type(T)

        A_k = V * T
        # print A_k

        spectra_A[k] = A_k

    # to compute the A_k where k is not coset leader
    for i in I:
        for j in range(1, I[i]):
            spectra_A[(i * (2 ** j)) % N] = spectra_A[i] ** (2 ** j)
    # print alpha ** 6
    
    return spectra_A



if __name__ == '__main__':
    seq = [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0]
    print dft(seq)
