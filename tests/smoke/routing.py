import os
import tempfile

import pytest

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@pytest.fixture
def status():
    for rule in app.url_map.iter_rules():
        with app.test_client() as client:
            client.get(str(rule))
