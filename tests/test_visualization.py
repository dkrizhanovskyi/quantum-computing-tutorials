import unittest
from tools.visualization import plot_results, run_circuit_and_plot
from qiskit_aer import Aer
from qiskit import QuantumCircuit

class TestVisualization(unittest.TestCase):

    def test_plot_results(self):
        backend = Aer.get_backend('qasm_simulator')
        qc = QuantumCircuit(2, 2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure([0, 1], [0, 1])

        job = backend.run(qc)
        result = job.result()
        plot = plot_results(result)
        self.assertIsNotNone(plot)

    def test_run_circuit_and_plot(self):
        try:
            run_circuit_and_plot()
        except Exception as e:
            self.fail(f"run_circuit_and_plot failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
