## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *
from ket import code_ket
import math
## Uncomment the next line to see diagrams when running in a notebook
#%matplotlib inline

## Example 4-1: Basic Teleportation

# Set up the program
alice = quant()
ep    = quant()
bob   = quant()

# entangle
H(ep)
cnot(ep, bob)

# prep payload
with around(H, alice):
    RZ(math.radians(45), alice)

# send
cnot(alice, ep)
H(alice)
alice_c = measure(alice)
ep_c = measure(ep)

# receive
@code_ket
def receive():
    if ep_c == 1:
        X(bob)
    if alice_c == 1:
        Z(bob)
receive()

# verify
with around(H, bob):
    RZ(math.radians(-45), bob)

bob_c = measure(bob)
outputstate = dump(alice + ep + bob)

## That's the program. Everything below runs.

print(f'result: {alice_c.value=}, {ep_c.value=}, {bob_c.value=}')

print(outputstate.show())
#from pprint import pprint
#pprint(quantum_code_last())
