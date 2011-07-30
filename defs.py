#!/usr/bin/env sage

from sage.all import *

TheFiniteField = GF(2)
ThePolynomialRing = TheFiniteField['X']
(X,) = ThePolynomialRing._first_ngens(1)

if __name__ == '__main__':
    a = X + 1
    b = a * X

    print a, b
