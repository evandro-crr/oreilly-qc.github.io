## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *

## Example 3-4: Swap Test
# Set up the program
input1 = quant()
input2 = quant()
output = quant()

with around(H, output):
    ctrl(output, swap, input1, input2)
X(output)
output_c = measure(output)

outputstate = dump(input1 + input2 + output)

print('result:', output_c.value)

print(outputstate.show())
