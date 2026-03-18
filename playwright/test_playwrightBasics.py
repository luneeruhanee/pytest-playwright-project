import time

from playwright.sync_api import Page, expect, Playwright


def test_playwritght_basics(playwright): #playwright is fixture that from pytest playwright package and it is global fixture that you dont have to implement
    browser = playwright.chromium.launch(headless=False)# launching chromium engin
    context = browser.new_context() # open in Incognito window
    page = context.new_page() #open tap
    page.goto("https://www.google.com")# enter to the website

# Page for chromium headless mode, 1 single context
# if you want to run and show the browser you have to modify configuration --headed
#page u=is obj, Page is class from playwright
def test_playwritght_shortcut(page:Page): #when you run it will not show you the browser because page is headless = True
    page.goto("https://www.google.com")

#you can write css selector with #ID, .Class, tag name
def test_core_locatores(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("password:").fill("Learning@830$3mK")
    page.get_by_role("combobox").select_option("teach") #for dropdown you have to copy option value
    page.locator("#terms").check() #use #id or classname for checkbox
    page.get_by_role("link", name="terms and conditions").click() #use name for specific link
    page.get_by_role("button", name="Sign In").click() #use name for specific button
    #In the website after click on sing in btn you have to wait a few sec and the warning msg will show but you dont need to code that because playwright have auto waite until the text is displayed
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible() #to chek text incase user/name wrong, use expect....to_be_visible -->waiting for text to visible

def test_firefox(playwright: Playwright):
    firefox_browser = playwright.firefox.launch(headless=False) #launching browser
    page = firefox_browser.new_page() # open new page
    page.goto("https://rahulshettyacademy.com/loginpagePractise/") # enter URL
    page.get_by_label("username:").fill("rahulshettyacademy")
    page.get_by_label("password:").fill("Learning@830$3mK") #Password is Learning@830$3mK2
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()




