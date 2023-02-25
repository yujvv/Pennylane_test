import pennylane as qml
from pennylane import numpy as np
import time

n_wires = int(input("qubits:\n"))
wires = list(range(n_wires))
num_iterations = int(np.pi/4 * np.sqrt(2**n_wires))

def oracle(wires):
    qml.Hadamard(wires[2])
    qml.Toffoli(wires=[wires[0], wires[1], wires[2]])
    qml.Hadamard(wires[2])

dev = qml.device('default.qubit', wires=wires)

@qml.qnode(dev)
def GroverSearch(num_iterations):
    for wire in wires:
        qml.Hadamard(wire)

    for _ in range(num_iterations):
        oracle(wires)
        qml.templates.GroverOperator(wires=wires)
    return qml.probs(wires)

start_time = time.time()
res = GroverSearch(num_iterations=num_iterations)
end_time = time.time()

elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time*1000000, " microseconds\n")
print(res)
