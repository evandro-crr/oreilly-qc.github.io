## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *

## Example 3-1: Seperable Qubits
# Set up the program
qubit1 = quant()
qubit2 = quant()
qubit3 = quant()

H(qubit2)              # put it into a superposition of 0 and 1
H(qubit3)              # put it into a superposition of 0 and 1

outputstate = dump(qubit1 + qubit2 + qubit3)
print(outputstate.show())
