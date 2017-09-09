#!/usr/bin/env python3

def e(b):
    """
    Given a tic tac toe board b of arbitrary size, determine if X or O
    won.

    Board must be specified as a tuple of characters. Each character
    may be the letter "X", the letter "O", or any other character (such
    as a space) indicating an empty spot on the board. The tuple shall
    represent the board starting with the upper-left corner, proceeding
    to the upper-right corner, and with proceeding rows following.

    For example:
    XOX
    O X
    OOX
    is a 3x3 board in which X won and O did not win. It could be
    represented as ('X','O','X','O',' ','X','O','O','X').

    Returns a two-tuple of (boolean X won, boolean O won)
    """
    s=int(len(b)**.5) # importless square root for board size
    # Adapt the board for X or O with significant 1s and insignificant 0s.
    a=lambda p:int(''.join(str(int(s==p)) for s in b),base=2)
    return (w(a('X'),s),w(a('O'),s))

def w(b,s):
    """
    Given a tic tac toe board b of arbitrary size s, determine if 1 won.

    This is a helper function for e. If I wasn't trying to reduce the
    character count, this function's name would begin with an
    underscore.

    Board must be specified as an integer, the binary representation of
    which depicts the sequence of values, proceeding from the upper-left
    corner to the upper-right corner, with proceeding rows following.

    For example:
    101
    001
    110
    would be represented as 101001110, or decimal 334.

    The board must be a square, the length of which must be s.

    Every non-1 square must be 0.
    """
    h=lambda s,i:(2**s-1)<<(s*(i+1)-s) # horizontal win based on OEIS A090411
    v=lambda s,i:int(2**(s**2+i)/(2**s-1)) # vertical win based on OEIS A033138
    d=lambda i:int((2**i*2**i**2-1)/(2*2**i-1)) # slash win, OEIS A119408
    u=lambda i:int((2**i**2-2**i)/(2**i-2)) # backslash win, OEIS A244961
    r=lambda f,s:[f(s,i) for i in range(s)] # iteration helper
    return any(b&w==w for w in r(h,s)+r(v,s)+[d(s),u(s)])
