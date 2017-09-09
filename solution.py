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

    Returns a boolean value signifying whether 1 won.
    """
    # h calculates a horizontal win. It's based on OEIS A090411. There
    # are multiple horizontal wins possible per board: one per row. The
    # i parameter represents which row will be used for this win.
    h=lambda i:(2**s-1)<<(s*(i+1)-s)
    # v calculates a vertical win. It's based on OEIS A033138. There
    # are multiple vertical wins possible per board: one per column. The
    # i parameter represents which column will be used for this win.
    v=lambda i:int(2**(s**2+i)/(2**s-1))
    # r is an iteration helper for h and v. It collects each row or
    # column of possible wins, based on the board size s.
    r=lambda f:[f(i) for i in range(s)] # iteration helper
    # d is a diagonal win shaped like "/". It is OEIS A119408.
    d=int((2**s*2**s**2-1)/(2*2**s-1))
    # u is a diagonal win shaped like "\". It is OEIS A244961.
    u=int((2**s**2-2**s)/(2**s-2))
    # To determine if 1 won, we compare a bitwise And against each
    # possible win to the win itself. Any matches means 1 has won.
    return any(b&w==w for w in r(h)+r(v)+[d,u])
