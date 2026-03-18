import pytest
from pytest_bdd import given, when, then, scenarios, parsers

from PageObject.login import LoginPage
from utils.apiBaseFramwork import APIUtils

scenarios('features/orderTransaction.feature')

@pytest.fixture
def share_data():
    return {}

@given(parsers.parse('place the item with {username} and {password}'))
def place_item_order(playwright, username, password, share_data):
    user_credentials = {}
    user_credentials["user_email"] = username
    user_credentials["user_password"] = password
    api_utils = APIUtils()
    orderid = api_utils.create_order(playwright, user_credentials)
    share_data["orderid"] = orderid
@given('the user is on landing page')
def user_on_landing_page(browser_instance, share_data):
    login_page = LoginPage(browser_instance)
    login_page.navigate()
    share_data["login_page"] = login_page

@when(parsers.parse('I login with portal with {username} and {password}'))
def login_to_portal(username, password, share_data):
    login_page = share_data["login_page"]
    dashboard_page = login_page.login(username, password)
    share_data["dashboard_page"] = dashboard_page

@when('navigate to order page')
def navigate_to_order_page(share_data):
    dashboard_page = share_data["dashboard_page"]
    order_history_page = dashboard_page.select_order_nav_link()
    share_data["order_history_page"] = order_history_page


@when('select the orderID')
def select_orderID(share_data):
    order_history_page = share_data['order_history_page']
    orderid = share_data["orderid"]
    order_detail_page = order_history_page.select_order(orderid)
    share_data["order_detail_page"] = order_detail_page

@then('order message is successful display')
def order_successful_display(share_data):
    order_detail_page = share_data['order_detail_page']
    order_detail_page.verify_order_message()
