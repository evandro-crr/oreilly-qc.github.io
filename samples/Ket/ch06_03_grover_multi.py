## Programming Quantum Computers
##   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
##   O'Reilly Media
##
## More samples like this can be found at http://oreilly-qc.github.io
##
## A complete notebook of all Chapter 6 samples (including this one) can be found at
##  https://github.com/oreilly-qc/oreilly-qc.github.io/tree/master/samples/Qiskit

from ket import *

## Example 6-3: Multiple flipped entries

# Set up the program
reg = quant(4)


def main():
    n2f = [0,1,2]
    number_of_iterations = 5

    H(reg)

    for _ in range(number_of_iterations):
        # Flip the marked value
        for number_to_flip in n2f:
            phase_on(number_to_flip, reg)

        Grover(reg)

###############################################
# Some utility functions


def Grover(qreg):
    with around(H, reg):
        phase_on(0, qreg)


main()

# That's the program. Everything below runs and draws it.

outputstate = dump(reg)
print(outputstate.show('i'))

total_prob = sum(outputstate.probabilities)

print('Total probability: {}%'.format(int(round(total_prob * 100))))