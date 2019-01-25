// Programming Quantum Computers
//   by Eric Johnston, Nic Harrigan and Mercedes Gimeno-Segovia
//   O'Reilly Media

// To run this online, go to http://oreilly-qc.github.io?p=8-2

//Specify the size of output register - determines precision of our answer
var m = 4;
// Specify the size of input register that will speicfy our eigenstate
var n = 1;
// Setup
qc.reset(m + n);
var qout = qint.new(m, 'output');
var qin = qint.new(n, 'input');
// Initialize output register all zeros
qout.write(0);
// Initialize input register as eigenstate of HAD
qin.write(0);
qin.rotx(22.5);
qin.phase(180);

// Define our conditional unitary
function cont_u(qcontrol, qtarget, control_count) {
    // For Hadamard, we ony need to know if control_count is even or odd,
    // as applying HAD an even number of times does nothing.
    if (control_count & 1)
        qtarget.chadamard(null, ~0, qcontrol.bits(control_count));
}


function phase_est(q_in, q_out, cont_u)
{
    // Main phase estimation single run
    // HAD the output register
    q_out.had();

    // Apply conditional powers of u
    for (j = 0; j < q_out.numBits; j++)
        cont_u(q_out, q_in, 1 << j);

    // Inverse QFT on output register
    q_out.invQFT();
}

// Operate phase estimation primitive on registers
phase_est(qin, qout, cont_u);
// Read output register
qout.read()