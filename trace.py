#!/usr/bin/env sage

from sage.all import *

def trace(x, m = None):    
    """
    the original trace() function in sage might have some bugs
    I got "sage.libs.pari.gen.PariError"
    so instead I wrote a inefficient algorithm like this...
    """
    if None == m:
        m = x.parent().degree() # the extension

    result = 0    
    for i in range(m):
        result += (x ** (2 ** i))
    return GF(2)(result)


if __name__ == '__main__':
    field = GF(2**8, 'alpha')
    alpha = field.gen()
    print trace(alpha**5 + alpha + 1)
