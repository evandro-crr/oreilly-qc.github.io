# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

# Example 7-8: QFT rotating phases

# Set up the program
signal = quant(4)


def main():

    # Rotate kth state in register by k times 20 degrees
    phi = 20

    # First HAD so that we can see the result for all k values at once
    H(signal)

    # Apply 2^k phase operations to kth qubit
    for i in range(4):
        val = 1 << i
        for _ in range(val):
            RZ(math.radians(phi), signal[i])


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
