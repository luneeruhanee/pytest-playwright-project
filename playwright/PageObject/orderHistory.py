from .orderDetail import OrderDetailPage


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def select_order(self,orderid):
        row = self.page.locator("tr").filter(has_text=orderid)
        row.get_by_role("button", name="View").click()
        order_detail_page = OrderDetailPage(self.page)
        return order_detail_page
