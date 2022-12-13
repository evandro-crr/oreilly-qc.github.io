## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io

from ket import *

## Example 2-4: Quasntum Spy Hunter
# Set up the program
alice = quant()
fiber = quant()
bob   = quant()

# Use Alice's QPU to generate two random bits
with run():
    alice_had = measure(H(quant())).value
H(alice)
alice_val= measure(alice)

# Prepare Alice's qubit
if alice_had == 1:
    H(alice)

# Send the qubit!
swap(alice, fiber)

# Activate the spy
spy_is_present = True
if spy_is_present:
    spy_had = True
    if spy_had:
        H(fiber)
    fiber_val = measure(fiber)
    if spy_had:
        H(fiber)

# Use Bob's QPU to generate a random bit
with run():
    bob_had = measure(H(quant())).value

# Receive the qubit
swap(fiber, bob)
if bob_had == 1:
    H(bob)
bob_val = measure(bob)

outputstate = dump(alice + fiber + bob)

# Now Alice emails Bob to tell
# him her had setting and value.
# If the had setting matches and the
# value does not, there's a spy!
print(f'{alice_had=}, {alice_val.value=}, {fiber_val.value=}, {bob_had=}, {bob_val.value=}')
caught = False
if alice_had == bob_had:
    if alice_val.value != bob_val.value:
        print('Caught a spy!')
        caught = True
if not caught:
    print('No spies detected.')

print(outputstate.show())
