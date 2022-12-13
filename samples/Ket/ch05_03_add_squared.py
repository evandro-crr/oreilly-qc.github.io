# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

# Example 5-3: Add squared value of one qint to another

# Note that this looks different from the gates in the book, because
# we're building the operations from Toffoli gates

# Set up the program
a = quant(4)
b = quant(2)


def main():
    # initialization
    X(a[0])
    H(a[2])
    RZ(math.radians(45), a[2])
    X(b[0])
    H(b[1])
    RZ(math.radians(90), b[1])

    # Increment
    add_squared_qint(a, b)

###############################################
# Some utility functions


def add_squared_qint(qdest, rhs, condition_qubits=None):
    if condition_qubits is None:
        condition_qubits = []
    for bit in range(len(rhs)):
        slideMask = list(set(condition_qubits + [rhs[bit]]))
        add_qint(qdest, rhs, slideMask, bit)


def add_qint(qdest, rhs, condition_qubits=None, shiftRHS=0):
    if condition_qubits is None:
        condition_qubits = []
    for bit in range(len(rhs)):
        add_int(qdest, 1 << bit, list(
            set([rhs[bit]] + condition_qubits)), shiftRHS)


def add_int(qdest, rhs, condition_qubits=None, shiftRHS=0):
    if condition_qubits is None:
        condition_qubits = []
    reverse_to_subtract = False
    if rhs == 0:
        return
    elif rhs < 0:
        rhs = -rhs
        reverse_to_subtract = True
    rhs <<= shiftRHS
    ops = []
    add_val = int(rhs)
    condition_mask = (1 << len(qdest)) - 1

    add_val_mask = 1
    while add_val_mask <= add_val:
        cmask = condition_mask & ~(add_val_mask - 1)
        if add_val_mask & add_val:
            add_shift_mask = 1 << (len(qdest) - 1)
            while add_shift_mask >= add_val_mask:
                cmask &= ~add_shift_mask
                ops.append((add_shift_mask, cmask))
                add_shift_mask >>= 1
        condition_mask &= ~add_val_mask
        add_val_mask <<= 1
    if reverse_to_subtract:
        ops.reverse()
    for inst in ops:
        op_qubits = [x for x in condition_qubits]
        for i in range(len(qdest)):
            if inst[1] & (1 << i):
                op_qubits.append(qdest[i])
        for i in range(len(qdest)):
            if inst[0] & (1 << i):
                op_qubits.append(qdest[i])
        multi_cx(op_qubits)


def multi_cz(qubits):
    # This will perform a CCCCCZ on as many qubits as we want
    ctrl(qubits[:-1], Z, qubits[-1])


def multi_cx(qubits):
    # This will perform a CCCCCX with as many conditions as we want
    ctrl(qubits[:-1], X, qubits[-1])


main()

# That's the program. Everything below runs and draws it.

outputstate = dump(reversed(a+b))
print(outputstate.show('i'))