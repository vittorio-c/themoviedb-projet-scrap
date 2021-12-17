import os
import tempfile

import pytest
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_routing(client):
    for rule in app.url_map.iter_rules():
        rv = client.get(str(rule))
        assert b"good" == rv.data
