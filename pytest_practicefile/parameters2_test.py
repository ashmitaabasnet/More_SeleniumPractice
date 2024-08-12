"""Using Parametrize with Fixtures"""

import pytest

@pytest.fixture(params=[("chrome", "latest"), ("firefox", "92.0")])
def browser_setup(request):
    browser, version = request.param
    return browser, version

def test_browser_version(browser_setup):
    browser, version = browser_setup
    assert browser in ["chrome", "firefox"]
    assert version is not None
