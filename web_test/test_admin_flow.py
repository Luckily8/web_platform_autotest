import pytest
from selenium.webdriver.common.by import By
from .locators import LoginPage, DishPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # 新增

BASE_URL = "http://localhost:80"   # 实际地址视部署而定

def test_admin_full_flow(driver):
    # 1. 打开登录页并登录
    driver.get(f"{BASE_URL}")
    # time.sleep(1)
    # driver.find_element(getattr(By, LoginPage.username_input[0].upper()), LoginPage.username_input[1]).send_keys("admin")
    # driver.find_element(getattr(By, LoginPage.password_input[0].upper()), LoginPage.password_input[1]).send_keys("123456")
    driver.find_element(getattr(By, LoginPage.login_btn[0].upper()), LoginPage.login_btn[1]).click()
    # time.sleep(1)

    # 2. 跳转到菜单明细
    driver.find_element(getattr(By, DishPage.dish_detail_btn[0].upper()), DishPage.dish_detail_btn[1]).click() # 点击菜品明细按钮
    # 等待目标元素出现
    target_elem = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]/span')
        )
    )
    # 判断当前按钮文本
    current_text = target_elem.text
    if current_text == "停售":
        target_elem.click() # 点击停止销售按钮
        # 等待弹窗并确认 
        driver.find_element(getattr(By, DishPage.confirm_btn[0].upper()), DishPage.confirm_btn[1]).click() # 点击确认按钮
        # 操作后等待文本变为“启售”
        WebDriverWait(driver, 10).until(lambda d: target_elem.text == "启售")
        assert target_elem.text == "启售"
    elif current_text == "启售":
        target_elem.click() # 点击开始销售按钮
        # 等待弹窗并确认
        driver.find_element(getattr(By, DishPage.confirm_btn[0].upper()), DishPage.confirm_btn[1]).click() # 点击确认按钮
        # 操作后等待文本变为“停售”
        WebDriverWait(driver, 10).until(lambda d: target_elem.text == "停售")
        assert target_elem.text == "停售"
    else:
        raise AssertionError(f"未知按钮文本: {current_text}")