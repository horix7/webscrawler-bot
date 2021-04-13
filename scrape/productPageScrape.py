from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json 

PATH = "/home/paul/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://internationaldeliver.shop/collections/nike-dunk/products/dunk-low-sb-am90-infrared")
print(driver.title)

productImages = driver.find_elements_by_class_name("product-single__thumb")

productTittle = driver.find_element_by_class_name("product-single__title").get_attribute("innerText")
productDescription = driver.find_element_by_class_name("product-single__description").get_attribute("innerText")
productPrice = driver.find_element_by_class_name("money").get_attribute("innerText")


images = [image.get_attribute("src") for image in productImages]

print(productDescription)

productInfo = dict()
productInfo["title"] = "".join(productTittle.split("\n"))
productInfo["price"] = productPrice.split("RF")[0]
productInfo["description"] = productDescription
productInfo["imageUrl"] = images

print(productInfo)

with open('product.json', 'w') as f:
    json.dump(productInfo, f)



time.sleep(2)

driver.quit()
