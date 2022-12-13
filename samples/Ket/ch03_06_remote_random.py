## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *

# Example 3-6: Remote Randomness
# Set up the program
a = quant()
b = quant()

H(a)
## now prob of a is 50%
H(b)
T(b)
H(b)
## now prob of b is 15%
cnot(a, b)        # entangle a and b
## Now, you can read *either*
## qubit and get 50% prob.
## If the result is 0, then
## the prob of the *remaining*
## qubit is 15%, else it's 85%
a_c = measure(a)
b_c = measure(b)

outputstate = dump(a + b)

print('result:', a_c.value, b_c.value)

print(outputstate.show())
