import pytest
from playwright.sync_api import Page
fake_payload_response={"data":[], "message": "No Orders"}
#api call from browser ->api call contract sever response back to browser -> browser use response to generate html
def intercept_response(route):
    route.fulfill(
        json= fake_payload_response
    )


@pytest.mark.smoke
def test_network1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response) #Network Mocking test
    page.get_by_placeholder("email@example.com").fill("tohlee89@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Lunee@07081995")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)