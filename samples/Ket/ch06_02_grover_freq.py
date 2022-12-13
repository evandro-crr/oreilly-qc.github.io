# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

from ket import *

# Example 6-2: Repeated iterations
# (This code is the same as sample 6-1, and we encourage you to play with
# the number of repeat iterations)

# Set up the program
reg = quant(4)


def main():
    number_to_flip = 3
    number_of_iterations = 4

    H(reg)

    for _ in range(number_of_iterations):
        # Flip the marked value
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