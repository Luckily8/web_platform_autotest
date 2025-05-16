import requests
import pytest

# 使用pytest的参数化功能，分别用order_id为1和99999进行测试
@pytest.mark.parametrize("order_id", [10,99999])
def test_get_order_detail(base_url, token, order_id):
    # 构造订单详情的URL
    url = f"{base_url}/admin/order/details/{order_id}"
    # 设置请求头，包含认证token
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
    resp = requests.get(url, headers=headers, proxies=proxies)
    # 如果订单号为10，假设该订单存在
    if order_id == 10:
        # 断言返回状态码为200
        assert resp.status_code == 200
        # 断言返回内容中包含"orderId"字段
        assert "id" in resp.json()["data"]
    else:
        # 其他订单号（如99999）假设不存在，断言is None
        assert resp.json()["data"] is None
