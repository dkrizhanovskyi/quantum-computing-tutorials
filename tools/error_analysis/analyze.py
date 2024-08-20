from qiskit_ibm_runtime.fake_provider import FakeVigoV2
from qiskit.visualization import plot_error_map
from qiskit.providers import Backend
from typing import Any, List

def analyze_errors(backend: Backend) -> List[Any]:
    error_map = backend.properties().to_dict().get('qubits', [])
    plot_error_map(backend)
    return error_map
