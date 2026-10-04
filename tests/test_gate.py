from fastapi.testclient import TestClient
from aimlops.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'champion': 'churn', 'eval_passed': True, 'digest': 'sha256:1', 'image': 'ml:1'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'champion': 'churn', 'eval_passed': True, 'digest': 'sha256:1', 'image': 'ml:latest'}).json()
    assert bad["passed"] is False
    assert "image_tag_latest" in bad["failed"]
