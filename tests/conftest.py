import pytest
from app import App


@pytest.fixture(scope="session")
def app(request):
    app = App('firefox', request.config.getoption("--headless"))
    app.open()
    yield app
    app.close()

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', help='run selected browser', default='chrome')
    parser.addoption("--headless", action='store', help='run headless browser', default='f')
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


