import time

from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, username: str, password: str, **kwargs) -> Page:
        if "base_url" not in kwargs:
            raise ConnectionRefusedError
        self.page.goto(kwargs.get("base_url"))
        self.page.fill('#username', username)
        self.page.fill('#password', password)
        self.page.click("'登 录'")
        time.sleep(30)
        return self.page
