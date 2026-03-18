
import json
#pytest --browser_name chrome -m smock -n 3 --tracing on --html=report.html

import pytest
from playwright.sync_api import Playwright, expect

from PageObject.login import LoginPage
from PageObject.dashboard import DashboardPage
from utils.apiBaseFramwork import APIUtils
#JSON file -> util -> access into test
with open('data/credentials.json') as f:
        test_data = json.load(f)
        print(test_data)
        user_credentials_list = test_data['user_credentials']
@pytest.mark.parametrize('user_credentials', user_credentials_list) #user_credentials is parameter


@pytest.mark.smock
def test_e2e_web_api(playwright: Playwright, browser_instance, user_credentials): #user_credentials is fixture. so this fixture return to user_credentials parameter
    user_name = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    #Create order ->orderId
    api_utils = APIUtils()
    orderid = api_utils.create_order(playwright, user_credentials)

    login_page = LoginPage(browser_instance) #object for login class
    login_page.navigate()
    dashboard_page = login_page.login(user_name, user_password)

    order_history_page = dashboard_page.select_order_nav_link()
    order_detail_page = order_history_page.select_order(orderid)
    order_detail_page.verify_order_message()

