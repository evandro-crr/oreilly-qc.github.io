# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

from ket import *

# Example 5-6: CNOT Logic

# initialization
with quant() as c:
    X(c)
    r1 = measure(c, free=True).value

with quant(2) as (b, c):
    X(b)
    cnot(b, c)
    r2 = measure(b+c, free=True).value

with quant(3) as (a, b, c):
    X(a+b)
    ctrl(a+b, X, c)
    r3 = measure(a+b+c, free=True).value

# That's the program. Everything below runs and draws it.

print('results:', r1, f'{r2:02b}', f'{r3:03b}')
