import pytest
from perses.model.dashboard import Dashboard
from perses.model.datasource import Datasource


def test_node_exporter_full(request: pytest.FixtureRequest):
    filepath = request.path.parent.joinpath("testdata/node-exporter-full.json")
    Dashboard.model_validate_json(filepath.read_text())


def test_prometheus_demo(request: pytest.FixtureRequest):
    filepath = request.path.parent.joinpath("testdata/prometheus-demo.json")
    Datasource.model_validate_json(filepath.read_text())
