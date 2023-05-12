import pytest
from app import App


@pytest.fixture(scope="session")
def app():
    app = App("firefox")
    app.open()
    yield app
    app.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--headless")
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

