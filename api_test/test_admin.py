import requests
import pytest
"""
This module contains automated tests for the admin login and user information retrieval endpoints
of a web application using the `requests` library.
Functions:
    test_admin_login(base_url):
        测试管理员登录接口。
        参数:
            base_url (str): API 的基础 URL。
        步骤:
            1. 构造管理员登录的请求 URL。
            2. 使用测试用户名和密码发送 POST 请求。
            3. 断言响应状态码为 200。
            4. 断言响应体中包含 "token" 字段，表示登录成功并返回了令牌。
    test_user_info(base_url, token):
        测试获取用户信息接口。
        参数:
            base_url (str): API 的基础 URL。
            token (str): 登录后获取的认证令牌。
        步骤:
            1. 构造用户信息请求的 URL。
            2. 在请求头中添加 Bearer 认证令牌。
            3. 发送 GET 请求获取用户信息。
            4. 断言响应状态码为 200。
            5. 断言响应体中的 "username" 字段为 "testuser"，验证用户信息正确。
"""




def test_admin_login(base_url):
    url = f"{base_url}/admin/employee/login"  # 构造管理员登录接口的URL
    data = {"username": "bajiang", "password": "123456"}  # 登录所需的用户名和密码
    resp = requests.post(url, json=data)  # 发送POST请求进行登录
    assert resp.status_code == 200  # 断言响应状态码为200，表示请求成功
    assert "token" in resp.json()["data"]

@pytest.mark.parametrize("user_id", [8])
def test_user_info(base_url, token, user_id):
    url = f"{base_url}/admin/employee/{user_id}"  # 构造获取用户信息的接口URL
    headers = {
        "token": f"{token}",
        "Accept": "*/*",
        "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
        "Host": "localhost:8080",
        "Connection": "keep-alive"
    }
    proxies = {
        "http": "http://127.0.0.1:8866",
        "https": "http://127.0.0.1:8866"
    }
    resp = requests.get(url, headers=headers, proxies=proxies)  # 发送GET请求获取用户信息
    assert resp.status_code == 200  # 断言响应状态码为200
    assert resp.json()["data"]["username"] == "bajiang"  # 断言返回的用户名为"bajiang"