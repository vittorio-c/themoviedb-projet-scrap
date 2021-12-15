import os
import tempfile

import pytest

from flask import Flask, redirect, render_template, request
from flaskr import create_app
from flaskr.db import init_db

app = Flask(__name__)

@pytest.fixture
def status():
    for rule in app.url_map.iter_rules():
        with app.test_client() as client:
            route = client.get(str(rule))
            
            return request.path . route.status_code
