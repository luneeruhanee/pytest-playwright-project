import time

from playwright.sync_api import Page, expect


def test_ui_check(page:Page):
    #hide/display , placeholder
    global price_col_value
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible() # check that element hide/show is visible in the web
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()



    #Alert box
    page.on("dialog", lambda dialog:dialog.accept()) #if there is an event dialog happen it will accept it, lambda is key word for writing 1 line anonymous function
    page.get_by_role("button", name="Confirm").click()


    #Mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()


    #Frame handle
    page_fram= page.frame_locator("#courses-iframe")# access to the frame
    page_fram.get_by_role("link", name="All Access plan").click() # page_fram is obj so whatever you do will happen inside of Frame only
    expect(page_fram.locator("body")).to_contain_text("Happy Subscibers") #check that in the body there is wording Happy Subscibers or not

    #web table handle
    #check the price of rice is equal to 37
    # identify rice row
    # identify price column
    # extrac the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    for index in range(page.locator("th").count()):  # loop every column header
        if page.locator("th").nth(index).filter(has_text="Price").count() > 0:
            price_col_value = index
            print(f"Price column value is: {price_col_value}")
            break

    rice_row = page.locator("tr").filter(has_text="Rice")
    expect(rice_row.locator("td").nth(price_col_value)).to_contain_text("37")
