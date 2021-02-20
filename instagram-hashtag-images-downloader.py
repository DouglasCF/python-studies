from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget

driver = webdriver.Chrome()
driver.get("http://www.instagram.com")

username = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
username.send_keys("go.droid")
password.clear()
password.send_keys("password")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button[type='submit']")
)).click()
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]')
)).click()
WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
    (By.XPATH, '//button[contains(text(), "Not Now")]')
)).click()

searchbox = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()

keyword = '#cat'

searchbox.send_keys(keyword)

time.sleep(3)
link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(@href, '/" + keyword[1:]+"/')]")))
link.click()

n_scrolls = 2
for j in range(n_scrolls):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword)

os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
