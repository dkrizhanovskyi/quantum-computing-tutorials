from qiskit_aer import Aer
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit.result import Result
from typing import Any

def plot_results(results: Result) -> Any:
    """
    Plot the results of a quantum circuit execution.

    Args:
        results (Result): The result object from a quantum circuit execution.

    Returns:
        Any: The generated plot object (usually a matplotlib figure).
    """
    counts = results.get_counts()
    return plot_histogram(counts)

def run_circuit_and_plot():
    """
    Create a quantum circuit, run it on a simulator, and plot the results.
    """
    backend = Aer.get_backend('qasm_simulator')
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])

    job = backend.run(qc)
    result = job.result()
    plot_results(result)
