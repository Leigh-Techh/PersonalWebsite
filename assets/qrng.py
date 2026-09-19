from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister

# Define 1 Qubit and 1 Classical Bit
qr = QuantumRegister(1, "q")
cr = ClassicalRegister(1, "c")
qc = QuantumCircuit(qr, cr)

# Apply Hadamard gate to put qubit in superposition
qc.h(qr[0])

# Measure qubit state into classical bit
qc.measure(qr[0], cr[0])

# Draw the circuit
print(qc.draw(output="text"))

from qiskit_aer import AerSimulator

# Initialize Aer Simulator
simulator = AerSimulator()


def generate_quantum_bit():
    # Run circuit once (shots=1)
    result = simulator.run(qc, shots=1).result()
    counts = result.get_counts()
    # Extract measured bit ('0' or '1')
    return list(counts.keys())[0]


def generate_quantum_int(num_bits=8):
    bit_string = "".join([generate_quantum_bit() for _ in range(num_bits)])
    return int(bit_string, 2), bit_string


# Example: Generate an 8-bit integer
quantum_num, bit_str = generate_quantum_int(8)
print(f"Binary: {bit_str} | Integer: {quantum_num}")
