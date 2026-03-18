import time

from playwright.sync_api import Page, expect
from pygments.lexer import words


def test_ui_validation_dynamic_script(page:Page):
    # add iphonex , Nokia edd to cart and verify 2 item showing in the cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("password:").fill("Learning@830$3mK2")  # Password is Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphone_product =page.locator("app-card").filter(has_text="iphone X") # css selector by name tage which is app-card, based on website there is 4 app-card name tag so it is not uniq so use filter(has_text) in order to filter only text that mach with iphone X
    iphone_product.get_by_role("button").click() #it will select btn only in iphone x section because iphone_product.get_by_role if page.get_by_role it will select all btn in entire page
    nokia_product =page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_product.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2) # css selector by using .class which is .media-body
    time.sleep(5)

#handel child browser
def test_child_window_handel(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as new_page_info: # expect_popup is the method will get trigger only when you have an event called a new window getting open
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click() #new page
        child_page = new_page_info.value
        text = child_page.locator(".im-para.red").text_content()
        print(text) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        words= text.split("at") #[0]= Please email us, [1]= mentor@rahulshettyacademy.com with below template to receive response
        email= words[1].strip().split(" ")[0] # make the value in index 1 split with space , [0] = mentor@rahulshettyacademy.com, [1]= with below template to receive response
        assert email == "mentor@rahulshettyacademy.com"