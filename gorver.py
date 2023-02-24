import pennylane as qml
from pennylane import numpy as np
import time

# Define the number of qubits and the number of iterations
num_qubits = 4
# the size of the database is 2^3 = 8
num_iterations = int(np.pi/4 * np.sqrt(2**num_qubits))

# Initialize the qubits in the |0⟩ state
dev = qml.device("default.qubit", wires=num_qubits)

@qml.qnode(dev)
def search_algorithm(params):
    # Apply the Hadamard gate to all qubits
    for i in range(num_qubits):
        qml.Hadamard(wires=i)

    # Perform the Grover iteration
    for _ in range(num_iterations):
        # Apply the Oracle (marked state is |101⟩)
        qml.CNOT(wires=[1, 2])
        qml.CZ(wires=[0, 1])
        qml.CNOT(wires=[1, 2])

        # Apply the Diffusion operator
        for i in range(num_qubits):
            qml.Hadamard(wires=i)
        qml.PhaseShift(np.pi/4, wires=1)
        qml.PhaseShift(np.pi/4, wires=2)
        qml.PhaseShift(np.pi/4, wires=0)
        for i in range(num_qubits):
            qml.Hadamard(wires=i)
    
    # Measure the qubits
    return qml.probs(wires=range(num_qubits))

# angles of pi/4 provide an equal superposition of states
initial_angles = [np.pi/4, np.pi/4, np.pi/4]

start_time = time.time()

print(search_algorithm(initial_angles))

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time*1000000, " microseconds")



