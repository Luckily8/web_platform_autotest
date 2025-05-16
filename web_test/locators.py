# 页面元素定位，便于维护
class LoginPage:
    username_input = ('xpath', '//*[@id="app"]/div/div/div/form/div[2]/div/div/input')  # 用户名输入框
    password_input = ('xpath', '//*[@id="app"]/div/div/div/form/div[3]/div/div/input')  # 密码输入框
    login_btn = ('xpath', '//*[@id="app"]/div/div/div/form/div[4]/div/button')  # 登录按钮

class DishPage:
    dish_detail_btn = ('xpath', '//*[@id="app"]/div/div[2]/section/div/div[3]/div[1]/h2/span/a')  # 菜品明细按钮
    stop_sell_btn = ('xpath', '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]/span')  # 停止销售按钮
    start_sell_btn = ('xpath', '//*[@id="app"]/div/div[2]/section/div/div/div[2]/div[3]/table/tbody/tr[1]/td[8]/div/button[3]/span')  # 开始销售按钮
    confirm_btn = ('xpath', '/html/body/div[2]/div/div[3]/button[2]/span')  # 确认按钮
