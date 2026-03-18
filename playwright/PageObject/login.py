from .dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):
        self.page = page #self.page is valuable class

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")


    def login(self, user_name, user_password):
        self.page.get_by_placeholder("email@example.com").fill(user_name)
        self.page.get_by_placeholder("enter your passsword").fill(user_password)
        self.page.get_by_role("button", name="Login").click()
        dashboard_page = DashboardPage(self.page) # after click login you know exactly will redirect to dashboard page
        return dashboard_page

