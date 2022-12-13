## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

## This sample demonstrates root-of-not.

from ket import *
import math

## Example 2-3: Root-of-not
# Set up the program
reg = quant()

# One root-of-not gate
with around(H, reg):
    RZ(math.radians(-90), reg)
# One root-of-not gate
with around(H, reg):
    RZ(math.radians(-90), reg)

outputstate = dump(reg)
print(outputstate.show())
