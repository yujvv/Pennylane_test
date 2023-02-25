import random
import time
import pennylane as qml

# Define the circuit
wires_nums = int(input("qubits:\n"))
dev = qml.device('default.qubit', wires=wires_nums)

# Define some commonly used quantum gates as PennyLane functions
gates = {
    "X": {'gate':qml.PauliX,'wires':1},
    "Y": {'gate':qml.PauliY,'wires':1},
    "Z": {'gate':qml.PauliZ,'wires':1},
    "H": {'gate':qml.Hadamard,'wires':1},
    "vCNOT": {'gate':qml.S,'wires':1}
    # "P": {'gate':qml.PhaseShift,'wires':1},
    # "CNOT": {'gate':qml.CNOT,'wires':2},
    # "CZ": {'gate':qml.CZ,'wires':2},
    # "SWAP": {'gate':qml.SWAP,'wires':2}
}


# Define a function that randomly chooses and returns a gate
def get_random_gate():
    gate_name = random.choice(list(gates.keys()))
    return gates[gate_name]

# Define the function to apply gates and measure the time
def apply_gates(num_gates):
    # Create an empty list to store the gates
    gates_list = []

    # Generate the random gates and add them to the list
    for i in range(num_gates):
        gates_list.append(get_random_gate())

    # Record the start time
    start_time = time.time()

    # Apply the gates sequentially
    @qml.qnode(dev)
    def circuit():
        for i in range(num_gates):
            for j in range(wires_nums):
                gates_list[i]['gate'](wires=j)
            # gates_list[i]['gate'](wires=range(gates_list[i]['wires']))
            # print("Applying {} gate on wires {}".format(gates_list[i]['gate'].__name__, gates_list[i]['wires']))
            print("Applying {} gate on wires".format(gates_list[i]['gate'].__name__))
#         return qml.probs(wires=range(gates_list[i]['wires']))
        return
    circuit()
    # Record the end time
    end_time = time.time()

    # Calculate and print the execution time
    elapsed_time = end_time - start_time
    print("Elapsed time: ", elapsed_time, "seconds")

if __name__ == '__main__':
    num_gates = int(input("gates:\n"))
    # num_gates = 4
    apply_gates(num_gates)
