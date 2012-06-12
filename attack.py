#!/usr/bin/env sage

from sage.all import *

import os

from dft import dft
from lfsr import lfsr
from bma import bma
from coset import coset
from trace import trace

def dft_attack(seq_s, fun_f, fun_g):
    n = fun_f.degree()
    field = GF(2 ** n, name = 'gamma', modulus = fun_f)
    gamma = field.gen()

    seq_b_iv = []
    for i in range(n):
        seq_b_iv.append(trace(gamma ** i))
    seq_b_generator = lfsr(seq_b_iv, fun_f)
    seq_b = []
    for i in range(2 ** n - 1):
        seq_b.append(seq_b_generator.next())
    # print 'seq_b', seq_b

    seq_a = []
    seq_b_doubled = seq_b * 2 # for ease of programming
    for i in range(2 ** n - 1):
        seq_a.append(GF(2)(fun_g(seq_b_doubled[i : (i + n)])))

    fun_p = bma(seq_a)
    if len(seq_s) < fun_p.degree():
        os.stderr.write("algorithm failed\n")
        os.exit(-1)

    # 2
    coset_leaders = coset(2 ** n - 1)
    for k in coset_leaders: # coset() is changed?
        if 1 == gcd(k, 2 ** n - 1) and k is not 1:
            break
    # k_inverse = field(k).pth_power(-1) # not right?
    for i in range(2 ** n - 1):
        if (i * k) % (2 ** n - 1) == 1:
            k_inverse = i
            break
    #print 'k_inverse', k_inverse


    # 3
    # print 'seq_a', seq_a
    # print type(seq_a[0])
    (A_k, S_k) = dft(seq_s, seq_a)
    # print 'A_k', A_k

    # online phase
    # 1
    # print 'seq_s', seq_s 
    # two dft computations are combined now
    # print 'S_k', S_k

    # 2
    # print 'k', k
    # print 'k_inverse', k_inverse
    # k_inverse = 13
    gamma_tau = (S_k[k] * (A_k[k] ** (-1))) ** (k_inverse)

    # print gamma_tau
    # 3
    result_u = []
    for i in range(n):
        result_u.append(trace(gamma_tau * (gamma_tau.parent().gen() ** i)))

    return result_u


if __name__ == '__main__':
    seq_s = [1, 0, 1, 1, 1, 0, 1, 0, 0, 0]

    polynomial_ring = GF(2)['X']
    X = polynomial_ring.gen()
    fun_f = X ** 4 + X + 1
    # print fun_f
    # print fun_f.is_primitive()

    # x0 + x0x1 + x3 + x0x3 + x0x1x3 + x0x2x3
    fun_g = lambda x: x[0] + x[0] * x[1] + x[3] + x[0] * x[3] + x[0] * x[1] * x[3] + x[0] * x[2] * x[3]

    print 'The initial states are'
    print dft_attack(seq_s, fun_f, fun_g)
