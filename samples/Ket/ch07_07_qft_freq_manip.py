# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

# Example 7-7: Frequency manipulation

# Set up the program
signal = quant(4)


def main():
    # Prepare a complex sinuisoidal signal
    freq = 2
    for i in range(len(signal)):
        if (1 << i) & freq:
            X(signal[i])
    adj(QFT, signal)

    # Move to frequency space with QFT
    with around(QFT, signal):
        # Increase the frequency of signal
        add_int(signal, 1)
        # Move back from frequency space


def add_int(qdest, rhs):
    reverse_to_subtract = False
    if rhs == 0:
        return
    elif rhs < 0:
        rhs = -rhs
        reverse_to_subtract = True
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
        op_qubits = []
        for i in range(len(qdest)):
            if inst[1] & (1 << i):
                op_qubits.append(qdest[i])
        for i in range(len(qdest)):
            if inst[0] & (1 << i):
                op_qubits.append(qdest[i])
        ctrl(op_qubits[:-1], X, op_qubits[-1])


def QFT(qreg):
    # This QFT implementation is adapted from IBM's sample:
    # https://github.com/Qiskit/qiskit-terra/blob/master/examples/python/qft.py
    # ...with a few adjustments to match the book QFT implementation exactly
    n = len(qreg)
    for j in range(n):
        for k in range(j):
            ctrl(qreg[n-j-1], phase(-math.pi/float(2**(j-k))), qreg[n-k-1])
        H(qreg[n-j-1])
    # Now finish the QFT by reversing the order of the qubits
    for j in range(n//2):
        swap(qreg[j], qreg[n-j-1])


main()

# That's the program. Everything below runs and draws it.

outputstate = dump(reversed(signal))
print(outputstate.show('i'))
