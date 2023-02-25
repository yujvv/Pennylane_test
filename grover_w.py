import pennylane as qml
from pennylane import numpy as np
import time
from datetime import datetime

grover_qubit = [10, 12, 14, 15, 16]
# grover_qubit = [3, 4]

def grover_test(n_wires):
    # n_wires = int(input("qubits:\n"))
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
    return elapsed_time
    # print("Elapsed time: ", elapsed_time*1000000, " microseconds\n")
    # print(res)

if __name__ == '__main__':
    res = []
    for i in grover_qubit:
        res.append(grover_test(i))
    print(res)
    with open('grover_results.txt', 'a') as f:
        print(res, file=f)
        time.sleep(3)
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M")
        print(formatted_time, file=f)



