from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Create order ->orderId
    api_utils = APIUtils()
    orderid = api_utils.create_order(playwright)
    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("tohlee89@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Lunee@07081995")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    #order history page -> order is present
    row = page.locator("tr").filter(has_text=orderid)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()
