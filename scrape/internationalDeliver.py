from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/paul/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://internationaldeliver.shop")
print(driver.title)

elements  = driver.find_elements_by_class_name("site-nav__dropdown-link")

collections = list()

for elem in elements:
    collections.append(elem.get_attribute("innerText"))

print(collections)

time.sleep(2)

driver.quit()
