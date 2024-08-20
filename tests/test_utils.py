import unittest
from tools.utils import initialize_qubit, apply_hadamard
from qiskit import QuantumCircuit

class TestUtils(unittest.TestCase):

    def test_initialize_qubit(self):
        qc = initialize_qubit()
        self.assertIsInstance(qc, QuantumCircuit)
        self.assertEqual(qc.num_qubits, 1)

    def test_apply_hadamard(self):
        qc = initialize_qubit()
        qc = apply_hadamard(qc)
        self.assertEqual(qc.data[0].operation.name, 'h')

if __name__ == '__main__':
    unittest.main()
