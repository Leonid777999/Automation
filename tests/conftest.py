import pytest
from app import App


@pytest.fixture(scope="session")
def app(request):
    app = App(request.config.getoption("--headless"))
    app.open()
    yield app
    app.close()


def pytest_addoption(parser):
    parser.addoption("--headless", action='store', help='run browser', default='f')
