import pytest
from service.common.login import LoginPage

"""
function：每一个函数或方法都会调用
class：每一个类调用一次，一个类可以有多个方法
module：每一个.py文件调用一次，该文件内又有多个function和class
session：是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
"""


@pytest.fixture()
def session(page):
    return LoginPage(page).login(
        username='18886885',
        password='Admin@123',
        base_url='http://172.23.16.13:8888/oauth/login',
    )


def pytest_sessionstart():
    ...


def pytest_sessionfinish(session):
    ...


@pytest.hookimpl(hookwrapper=True)
def pytest_collection():
    yield
