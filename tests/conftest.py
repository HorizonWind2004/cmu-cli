"""Block unmocked Requests and subprocess.run; not a general OS sandbox."""

import pytest


@pytest.fixture(autouse=True)
def offline(monkeypatch):
    import subprocess

    import requests

    def forbidden(*args, **kwargs):
        raise AssertionError("Unmocked external access is forbidden in offline tests")

    monkeypatch.setattr(requests.sessions.Session, "request", forbidden)
    monkeypatch.setattr(subprocess, "run", forbidden)
    for name in [
        "CMUCW_CANVAS_TOKEN",
        "CMUCW_ALLOW_BROWSER_COOKIES",
        "CMUCW_EDGE_COOKIE_FILE",
        "CMUCW_COOKIE_HOSTS",
        "CMUCW_CONFIG",
    ]:
        monkeypatch.delenv(name, raising=False)
