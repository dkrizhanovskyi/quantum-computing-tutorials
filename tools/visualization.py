# Visualization tools for quantum circuits
from qiskit.visualization import plot_histogram

def plot_results(results):
    """Plot the results of a quantum circuit execution"""
    plot_histogram(results.get_counts())
