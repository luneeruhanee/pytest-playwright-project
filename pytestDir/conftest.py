# it is like per set up before start testing,
# scope = function is run before for every test function by default,
# scope = module is it run only once before all test function in the same file
# scope = class is it run Once per test class
# scope = session is it run Once for whole test run
import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def pre_setup_work():
    print("I set up browser instance")
