from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
# Create a new instance of the Chrome driver
driver = webdriver.Firefox()
niche = "agro"
# Navigate to a website
driver.get(f"https://www.tiktok.com/search?q={niche}")

time.sleep(10)
videos= driver.find_elements(By.TAG_NAME, "video")

for video in videos:
  print(video.get_attribute("src"))import requests

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'hx-current-url': 'https://ssstik.io/en-1',
    'hx-request': 'true',
    'hx-target': 'target',
    'hx-trigger': '_gcaptcha_pt',
    'origin': 'https://ssstik.io',
    'priority': 'u=1, i',
    'referer': 'https://ssstik.io/en-1',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
}

params = {
    'url': 'dl',
}

data = {
    'id': 'https://www.tiktok.com/@parana_agricola/video/7316301286557732102?is_from_webapp=1&sender_device=pc&web_id=7388290703694415365',
    'locale': 'en',
    'tt': 'emU4Tkhj',
}

response = requests.post('https://ssstik.io/abc', params=params, headers=headers, data=data)