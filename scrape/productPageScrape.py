from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "/home/paul/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://internationaldeliver.shop/collections/nike-dunk/products/dunk-low-sb-am90-infrared")
print(driver.title)

productImages = driver.find_elements_by_class_name("product-single__thumb")

images = [image.get_attribute("src") for image in productImages]

print(images)
time.sleep(2)

driver.quit()
