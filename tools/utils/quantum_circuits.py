from qiskit import QuantumCircuit

def initialize_qubit() -> QuantumCircuit:
    qc = QuantumCircuit(1)
    return qc

def apply_hadamard(qc: QuantumCircuit, qubit: int = 0) -> QuantumCircuit:
    qc.h(qubit)
    return qc
