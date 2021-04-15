from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json 

allProductsLinks = json.load(open("data.json"))

PATH = "/home/paul/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

productArray = list()

for everyLink in allProductsLinks:
    driver.get(everyLink["link"])

    productImages = driver.find_elements_by_class_name("product-single__photo")

    productTittle = driver.find_element_by_class_name("product-single__title").get_attribute("innerText")
    productDescription = driver.find_element_by_class_name("product-single__description").get_attribute("innerText")
    productPrice = driver.find_element_by_class_name("money").get_attribute("innerText")


    images = [image.get_attribute("src").split("?v=")[0] for image in productImages]


    productInfo = dict()
    productInfo["title"] = "".join(productTittle.split("\n"))
    productInfo["price"] = productPrice.split("RF")[0]
    productInfo["description"] = productDescription
    setimages =  [i for j, i in enumerate(images) if i not in images[:j]]
    setimages[0] = setimages[1]
    setimages[1] = setimages[0]
    productInfo["imageUrl"] = json.dumps(images)
    productInfo["collection"] = everyLink["collection"]

    productArray.append(productInfo)

with open('allProducts.json', 'w') as f:
    json.dump(productArray, f)


time.sleep(2)

driver.quit()
