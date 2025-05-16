# autotest 目录说明

本目录用于存放接口自动化测试脚本，基于 pytest+requests 进行开发，支持 Allure 测试报告。

## 环境准备

```bash
cd autotest
python -m venv venv
source venv/bin/activate  # Windows下为 venv\Scripts\activate
pip install -r requirements.txt
```

## 用例执行

```bash
pytest --alluredir=./results
allure serve ./results
```