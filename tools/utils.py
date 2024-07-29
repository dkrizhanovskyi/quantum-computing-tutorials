# Utility functions for quantum computing projects
from qiskit import QuantumCircuit

def initialize_qubit():
    """Initialize a single qubit quantum circuit"""
    qc = QuantumCircuit(1)
    return qc

def apply_hadamard(qc, qubit):
    """Apply a Hadamard gate to the specified qubit"""
    qc.h(qubit)
    return qc
