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
    collections.append(elem.get_attribute("href"))

# links = list()
# for collect in collections:
#     if len(collect.split(" ")) == 1:
#         links.append("https://internationaldeliver.shop/collections/" + collect)
#     else:
#         link = collect.split(" ")
#         link = "-".join(link)
#         links.append("https://internationaldeliver.shop/collections/" + link + "/" + link)

collectionWithLinks = list()

for link in collections: 
    driver.get(link)
    products = driver.find_elements_by_class_name("grid-product__meta")
    for product in products:
        collectionWithLinks.append({ "collection": "null-for-now", "link": product.get_attribute("href")})

print(collectionWithLinks)

time.sleep(2)

driver.quit()
