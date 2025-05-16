import pytest

@pytest.fixture(scope="session")
def base_url():
    # 配置后端服务基础地址
    return "http://localhost:8080"

@pytest.fixture(scope="session")
def token(base_url):
    # 登录获取JWT token（需根据实际登录接口调整）
    import requests
    login_url = f"{base_url}/admin/employee/login"
    data = {"username": "bajiang", "password": "123456"}
    resp = requests.post(login_url, json=data)
    return resp.json()["data"].get("token")