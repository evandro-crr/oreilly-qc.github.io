## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *
import math

## Example 3-3: Phase Kickback
# Set up the program
reg1 = quant(2)
reg2 = quant(1)

H(reg1)         # put a into reg1 superposition of 0,1,2,3
ctrl(reg1[0], phase(math.pi/4), reg2)
ctrl(reg1[1], phase(math.pi/2), reg2)

outputstate = dump(reg1 + reg2)
print(outputstate.show('b2:b1'))
