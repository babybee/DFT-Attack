TheFiniteField = GF(2)
ThePolynomialRing.<X> = TheFiniteField[]

def bma(s):    
    "using the notations in 'Shift-register synthesis and BCH decoding' by Massey"
    C = ThePolynomialRing(1)
    B = ThePolynomialRing(1)

    b = TheFiniteField(1)

    m = 1 # replacing the orignial notation, x
    L = 0

    for N in range(len(s)):
        d = TheFiniteField(s[N])
        for l in range(1, len(C.list())): # range(1, L + 1) will cause out-of-index error
            d += C.list()[l] * TheFiniteField(s[N - l])

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

    return C.reverse() # must be reversed in this notation
    # might have some problems?
    # because reverse() cannot gurantee the overall degree

if __name__ == '__main__':
    seq = (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0)
    pol = bma(seq)
    
    print 'The input sequence is', seq
    print 'Its characteristic polynomial is', pol