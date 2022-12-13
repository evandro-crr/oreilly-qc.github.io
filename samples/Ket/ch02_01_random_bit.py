## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

## This sample generates a single random bit.

from ket import *

## Example 2-1: Random bit
# Set up the program
reg = quant()

H(reg)               # put it into a superposition of 0 and 1
reg_c = measure(reg) # read the result as a digital bit
outputstate = dump(reg)

print('result:', reg_c.value)
print(outputstate.show())
