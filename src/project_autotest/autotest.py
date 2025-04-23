import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = os.path.join(os.path.dirname(__file__), "chromedriver.exe")
service = Service(driver_path)

# Запускаем браузер Chrome
driver = webdriver.Chrome(service=service)
driver.get("https://only.digital")

time.sleep(5)
footer = driver.find_element(By.TAG_NAME, "footer")
print("Footer was found")

links = footer.find_elements(By.TAG_NAME, "a")
if len(links) > 0:
    print("Links were found in the footer")
else:
    print("Links were not found in the footer")

buttons = footer.find_elements(By.TAG_NAME, "button")
if len(buttons) > 0:
    print("Buttons were found in the footer")
else:
    print("Buttons were not found in the footer")

images = footer.find_elements(By.TAG_NAME, "img")
if len(images) > 0:
    print("Images were found in the footer")
else:
    print("Images were not found in the footer")

driver.quit()