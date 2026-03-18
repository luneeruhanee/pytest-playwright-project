from playwright.sync_api import Page, Playwright, expect

from utils.apiBase import APIUtils


#api call from browser ->api call contract sever response back to browser -> browser use response to generate html

#the case is user cannot see order id that belong to others account

def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/client/#/dashboard/order-details/69b40c02f86ba51a6500a1a0") #this order id is belong to another account


def test_network2(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request) #mock request
    page.get_by_placeholder("email@example.com").fill("tohlee89@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Lunee@07081995")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright: Playwright):
    api_utils = APIUtils()
    get_token = api_utils.get_token(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #scrip to inject token in session local storage. bypass login
    page.add_init_script(f"""localStorage.setItem("token", "{get_token}")""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()