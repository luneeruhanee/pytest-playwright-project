# run test by using command
# run many file using pytest (keyword:test) every file have to named test
# run individual file using pytest(spce) +file name
# run particular test function using pytest(spce)file name::test function name
# if you want to display with log pytest(spce)file name::test function name -s
# if you want run specific group test function using pytest -m named tag
# if you want to run test case with some key word pytest -k keyword for example pytest -k web_api


#fixtures
import pytest


@pytest.fixture(scope="module")  # it is like per set up before start testing, scope = function is run before for every test function by default, scope = module/class is it run only once before all test function in the same file
def prework():
    print("I set up module instance")
    return "fail" #value will store in prework

@pytest.fixture(scope="function")
def second_work():
    print("I set up second work instance")
    yield #pause
    print("tear down validation")

@pytest.mark.smock # this is for named tag so tag named is smock
def test_firs_tcheck(prework, second_work):  # it will check per work function first then will test this function
    print("This is first test")
    assert prework == "fail"

@pytest.mark.skip #if you want to skip test function
def test_second_check(pre_setup_work, second_work):
    print("This is second test")
