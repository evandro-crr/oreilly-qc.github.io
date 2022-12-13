# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

# Example 7-3: QFT square wave

# Set up the program
signal = quant(4)


def main():
    # prepare the signal
    H(signal)
    RZ(math.radians(180), signal[1])

    QFT(signal)


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
