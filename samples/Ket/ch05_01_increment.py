## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

## Example 5-1: Increment and Decrement

## Note that this looks different from the gates in the book, because
## we're building the operations from Toffoli gates

# Set up the program
a =       quant(4)
scratch = quant(1)

def main():
    ## initialization
    X(a[0])
    H(a[2])
    RZ(math.radians(45), a[2])
    
    ## Increment
    add_int(a, 1)
    ## Decrement
    add_int(a, -1)

###############################################
## Some utility functions

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
        mask = 1
        for i in range(len(qdest)):
            if inst[1] & (1 << i):
                op_qubits.append(qdest[i])
        for i in range(len(qdest)):
            if inst[0] & (1 << i):
                op_qubits.append(qdest[i])
        ctrl(op_qubits[:-1], X, op_qubits[-1])

main()

## That's the program. Everything below runs and draws it.


outputstate = dump(reversed(a))
print(outputstate.show('i'))
