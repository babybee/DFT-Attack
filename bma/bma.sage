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
        d = TheFiniteField(0)
        print N, C, type(C)
        for l in range(L + 1):
            d += C.list()[l] * TheFiniteField(s[N - L + l])

        if d == 0:
            print '='
            m += 1
        else:
            if 2 * L > N:
                print '>'
                print C, d, b, B, m
                print d * (b ^ (-1)) * B.shift(m)
                C -= d * (b ^ (-1)) * B.shift(m)
                m += 1
            else:
                print '<'
                T = C
                C -= d * (b ^ (-1)) * B.shift(m)
                L = N + 1 - L
                B = T
                b = d
                m = 1

    return C

if __name__ == '__main__':
    seq = (0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0)
    pol = bma(seq)
    
    print 'The input sequence is %s.' % str(seq) 
    print 'Its characteristic polynomial is ', pol
