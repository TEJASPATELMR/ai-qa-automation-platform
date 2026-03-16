
import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def pw(request):
    playwright = Playwright()
    browser = playwright.chromium.launch()
    request.session.object_graph.update(browser=browser)
    yield browser
    browser.close()
