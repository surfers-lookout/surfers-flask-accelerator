import pytest
from main import create_app
from main.data.models import db

@pytest.fixture(scope="session")
def app():
    app = create_app('testing')
    return app


@pytest.fixture(scope='module')
def new_dummy(app):
    with app.app_context():
        from main.data.models import Dummy
        _dummy = Dummy(name='wibble',description='wobble')
        return _dummy


@pytest.fixture(scope='module')
def test_client(app):

    # Create a test client using the Flask application configured for testing
    with app.test_client() as testing_client:
        # Establish an application context
        with app.app_context():
            yield testing_client  # this is where the testing happens
