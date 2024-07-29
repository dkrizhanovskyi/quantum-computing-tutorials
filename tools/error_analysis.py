# Utility functions for quantum error analysis
from qiskit.visualization import plot_error_map

def analyze_errors(backend):
    """Analyze and plot the error map of a quantum backend"""
    error_map = backend.properties().to_dict()['qubits']
    plot_error_map(backend)
