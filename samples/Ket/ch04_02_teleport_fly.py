# Programming Quantum Computers
# by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
# O'Reilly Media
##
# More samples like this can be found at http://oreilly-qc.github.io

#######################################################
# Example 4-2: A Fly in the Teleporter
##
# This is a fun and horrifying example from the
# teleportation chapter.

from operator import attrgetter
from ket import *
from ket import code_ket

num_fly_qubits = 6  # this can be 6 or 8, for a mini-fly or full-fly.

# This is the left half of the pixels of the fly,
# encoded as an 8x16 array:
image8 = ['........',
          '...X....',
          '....X.XX',
          '.....XXX',
          '....XXXX',
          'XX...XXX',
          '..XXX.XX',
          '...X....',
          '..X...XX',
          '.X...XXX',
          'X....XXX',
          'X..XXXXX',
          '.XXX.XXX',
          '...X..XX',
          '..X.....',
          '........']

# This is the left half of the pixels of the fly,
# encoded as a 4x8 array:
image6 = ['..X.',
          '...X',
          'X.XX',
          '.X..',
          'X..X',
          'X..X',
          '.XX.',
          'X...']

image = image6 if num_fly_qubits == 6 else image8

# This is the classic teleport example, but with an interesting
# payload, and some controllable error.
teleport_error = 0.0  # <--- change this number to 0.1 or more
do_teleport = True  # Enables the teleporter

# Set up the program
fly = quant(num_fly_qubits)
epair1 = quant(num_fly_qubits)
epair2 = quant(num_fly_qubits)
scratch = epair1  # We only need scratch qubits during preparation
send0_c = [0]*num_fly_qubits
send1_c = [0]*num_fly_qubits

last_not = 0


def main():
    prepare_fly(fly)
    if do_teleport:
        entangle_pair(epair1, epair2)
        send_payload(fly, epair1, [send0_c, send1_c])
        apply_error(epair2, teleport_error)
        receive_payload(epair2, [send0_c, send1_c])


def entangle_pair(ep1, ep2):
    # Create all the entangled qubits we need to teleport this object.
    H(ep1)
    cnot(ep1, ep2)


def prepare_fly(fly):
    # Encode the fly pixels into relative phases in a
    # quantum superposition
    global last_not
    H(fly)
    for y in range(len(image)):
        for x in range(len(image[0])):
            if (image[y][x] == 'X'):
                pixel(fly, x + 0, y)
    # TODO: translate these lines
    for i in range(num_fly_qubits):
        if (1 << i) & last_not:
            X(fly[i])
    # Reflect to get both halves
    if num_fly_qubits == 8:
        cnot(fly[3], fly[0])
        cnot(fly[3], fly[1])
        cnot(fly[3], fly[2])
    else:
        cnot(fly[2], fly[0])
        cnot(fly[2], fly[1])

    # Grover to turn the phase diffs into amp diffs
    Grover(fly)

    # At this point, reading the "fly" register would be very likely
    # to return the coordinates of one of the pixels in the fly.


def pixel(obj, x, y):
    # Given x and y, flip the phase of one term
    # Note: last_not is used to avoid redundant NOT gates
    global last_not
    val = ~((y << (num_fly_qubits >> 1)) | x)
    for i in range(num_fly_qubits):
        if (1 << i) & (val ^ last_not):
            X(obj[i])
    last_not = val
    if num_fly_qubits == 8:
        multi_cz([obj[0], obj[1], obj[2], obj[4], obj[5], obj[6], obj[7]])
    else:
        multi_cz([obj[0], obj[1], obj[3], obj[4], obj[5]])


def send_payload(payload, ep, digital_bits):
    # Entangle the payload with half of the e-pair, and then vaporize it!
    cnot(payload, ep)
    H(payload)
    for i in range(num_fly_qubits):
        digital_bits[0][i] = measure(payload[i])
        digital_bits[1][i] = measure(ep[i])


def apply_error(qubits, error_severity):
    # Apply some unpredictable noise to the system
    RX(error_severity, qubits)


@code_ket
def receive_payload(ep, digital_bits):
    # Teleport receiver applies the correct operations based on
    # the digital data. Note that in this example we *could*
    # use postselection, but would only succeed once every 65,536
    # tries, on average.
    for i in range(num_fly_qubits):
        if digital_bits[1][i] == 1:
            X(ep[i])
        if digital_bits[0][i] == 1:
            Z(ep[i])


def Grover(qreg):
    with around([H, X], qreg):
        multi_cz(qreg)


def multi_cz(qubits):
    # This will perform a CCCCCZ on as many qubits as we want,
    # as long as we have enough scratch qubits
    ctrl(qubits[:-1], Z, qubits[-1])


main()

# That's the program. Everything below runs and draws it.
# TODO: A nice way to draw the fly here.

outputstate = dump(fly + epair1 + epair2)
exec_quantum()

print('Finished in {} seconds'.format(quantum_exec_time()))

print('results:', list(map(attrgetter("value"), send0_c)),
      list(map(attrgetter("value"), send1_c)))

print(outputstate.show())
