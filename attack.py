#!/usr/bin/env sage

from sage.all import *

from dft import dft
from lfsr import lfsr
from bma import bma
import os
from coset import coset

def dft_attack(seq_s, fun_f, fun_g):
    n = fun_f.degree()
    field = GF(2 ** n, 'alpha', fun_f)
    alpha = field.gen()

    seq_b_iv = []
    for i in range(n):
        seq_b_iv.append((alpha ** i).trace())
    seq_b_generator = lfsr(seq_b_iv, fun_f)
    seq_b = []
    for i in range(2 ** n - 1):
        seq_b.append(seq_b_generator.next())

    seq_a = []
    seq_b_double = seq_b * 2 # for ease of programming
    for i in range(2 ** n - 1):
        seq_a.append(fun_f(seq_b_double[i : (i + n)]))

    fun_p = bma(seq_a)
    if len(seq_s) < fun_p.degree():
        os.stderr.write("algorithm failed\n")
        os.exit(-1)

    # 2
    coset_leaders = coset(2 ** n - 1)
    for k in coset_leaders:
        if 1 == gcd(k, 2 ** n - 1):
            break
    k_inverse = field(k) ** (-1)

    # 3
    A_k = dft(seq_a)

    # online phase
    # 1
    S_k = dft(seq_s)

    # 2
    alpha_tau = (S_k(k) * (A_k(k) ** (-1))) ** (k_inverse)

    # 3
    result_u = []
    for i in range(n):
        result_u.append((alpha_tau * (alpha ** i)).trace())

    return result_u


if __name__ == '__main__':
    seq_s = (1, 0, 1, 1, 1, 0, 1, 0, 0, 0)

    polynomial_ring = GF(2)['X']
    X = polynomial_ring.gen()
    fun_f = X ** 4 + X + 1

    # what is the function g(...)
    fun_g = lambda state: state[0] * state[1]

    print dft_attack(seq_s, fun_f, fun_g)
