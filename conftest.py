import pytest
from app import App


@pytest.fixture(scope="session")
def app():
    app = App()
    app.open_self()
    yield app
    app.close_self()