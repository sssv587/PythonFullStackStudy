# 第三方:pillow    pip install
import requests
# import pillow

response = requests.get('https://www.12306.cn')
print(response.text)
