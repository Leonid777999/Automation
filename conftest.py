import pytest
from app import App


@pytest.fixture(scope="session")
def app():
    app = App()
    app.open()
    yield app
    app.close()