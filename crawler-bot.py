from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/paul/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("http://google.com/")
print(driver.title)

search = driver.find_element_by_class_name("gLFyf")

search.send_keys("testing googlw bots")
search.send_keys(Keys.RETURN)

time.sleep(10)

driver.quit()
