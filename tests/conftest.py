"""
Pytest configuration file with fixtures for testing the Flask application.
"""
import pytest
import sys
import os

# Add parent directory to path to import main module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app as flask_app


@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Set testing config
    flask_app.config['TESTING'] = True
    flask_app.config['DEBUG'] = False
    
    yield flask_app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """A test CLI runner for the app."""
    return app.test_cli_runner()
