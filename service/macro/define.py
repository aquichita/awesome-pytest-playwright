from playwright.sync_api import Page

from service.common.navigate import Navigate


class MacroDefine:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        Navigate(self.page).to(["TMS-流程引擎", "宏定义"])

    def create(
            self,
            xid: str,
            name: str
    ) -> Page:
        self.page.click("新建")
        self.page.fill("name='xid", xid)
        self.page.fill("name='name", name)
        self.page.click("确定")
        return self.page
