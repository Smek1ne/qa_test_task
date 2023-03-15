import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get('https://demoqa.com')

x = browser.find_element(By.XPATH, '//h5[text()="Elements"] //ancestor:: *[contains(@class, "top-card")]')
x.click()
# time.sleep(5)


browser.get("https://demoqa.com/checkbox")
y = browser.find_element(By.CSS_SELECTOR, '#item-1.active')
y.click()
y = browser.find_element(By.CSS_SELECTOR, '.rct-node-parent button')
y.click()

time.sleep(5)











