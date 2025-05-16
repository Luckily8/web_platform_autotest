import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="session")  # 定义一个pytest的fixture，作用域为session级别
def driver():
    options = Options()  # 创建Chrome浏览器的配置对象
    # options.add_argument("--headless")   # 添加无头模式参数，如需可视化，可注释掉此行
    driver = webdriver.Chrome(options=options)  # 启动Chrome浏览器
    driver.implicitly_wait(5)  # 设置隐式等待时间为5秒
    yield driver  # 返回driver对象，供测试用例使用
    driver.quit()  # 测试结束后关闭浏览器