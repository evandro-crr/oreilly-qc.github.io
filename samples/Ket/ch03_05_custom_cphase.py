## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

# Example 3-5: Custom conditional-phase
# Set up the program
reg = quant(2)

theta = math.pi / 2
H(reg)
with around(cnot(I, RZ(theta/2)), reg[0], reg[1]):
    RZ(-theta/2, reg[1])

ctrl(reg[0], RZ(theta), reg[1])

outputstate = dump(reg)
print(outputstate.show())
