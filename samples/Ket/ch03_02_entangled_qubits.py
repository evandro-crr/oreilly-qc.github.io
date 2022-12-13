## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *

## Example 3-2: Entangled Qubits
# Set up the program
a = quant()
b = quant()

H(a)              # put a into a superposition of 0 and 1
cnot(a, b)        # entangle a and b
a_c = measure(a)
b_c = measure(b)

outputstate = dump(a+b)

print('result:', a_c.value, b_c.value)

print(outputstate.show())
