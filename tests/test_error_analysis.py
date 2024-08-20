import unittest
from qiskit_ibm_runtime.fake_provider import FakeVigoV2
from tools.error_analysis import analyze_errors

class TestErrorAnalysis(unittest.TestCase):

    def test_analyze_errors(self):
        backend = FakeVigoV2()
        error_map = analyze_errors(backend)
        self.assertIsInstance(error_map, list)
        self.assertGreater(len(error_map), 0)

if __name__ == '__main__':
    unittest.main()
