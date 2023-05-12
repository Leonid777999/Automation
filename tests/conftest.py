import pytest
from app import App


@pytest.fixture(scope="session")
def app(request):
    app = App('chrome', request.config.getoption("--headless"))
    app.open()
    yield app
    app.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless", action='store', help='run headless browser', default='f')
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

