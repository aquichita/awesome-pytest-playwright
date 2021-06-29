import allure
from playwright.sync_api import Page
from typing import List


class Navigate:
    def __init__(self, page: Page):
        self.page = page

    def to(self, menus: List[str]) -> Page:
        with allure.step(f"导航: {menus}"):
            for menu in menus:
                self.page.click(f"'{menu}'")
        return self.page
