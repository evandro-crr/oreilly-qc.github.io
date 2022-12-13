## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *

## Example 2-2: Random byte
# Set up the program
reg = quant(8)

H(reg)               # put it into a superposition of 0 and 1
reg_c = measure(reg) # read the result as a digital bit

print('Random number:', reg_c.value)
