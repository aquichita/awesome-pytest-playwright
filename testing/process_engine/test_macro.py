import random
import time

import allure
from allure import description, epic, feature, severity, story
from allure_commons.types import Severity

from service.macro.define import MacroDefine


@epic("TMS-流程引擎")
@feature("流程配置")
@story("宏定义")
@severity(Severity.NORMAL)
@description("新建宏定义")
def test_create(session):
    with allure.step("1. 新建宏定义"):
        value = str(int(time.time()))
        MacroDefine(session).create(xid=value, name=value)
