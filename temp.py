from seleniumwire import webdriver
from seleniumwire.utils import decode
import json
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(
    "C:/Users/Nirman/AppData/Local/Programs/Python/Python37/chromedriver.exe")
# Go to the Google home page
driver.get('https://v3601506.v360.in/vision360.html?d=11914-516259491&z=1&surl=https%3a%2f%2fv3601506.v360.in%2f')

time.sleep(10)
# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        if request.url.startswith("https://v3601506.v360.in/imaged/"):
            print("url : ", request.url)
            body = decode(request.response.body, request.response.headers.get(
                'Content-Encoding', 'identity'))
            decode_body = body.decode('utf-8')
            json_data = json.loads(decode_body)
            print("json : ", body)
