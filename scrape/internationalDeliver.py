from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/home/paul/Documents/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://internationaldeliver.shop")
print(driver.title)

elements  = driver.find_elements_by_class_name("site-nav__dropdown-link")

collections = list()

for elem in elements[5:7]:
    collections.append({"name": elem.get_attribute("innerText"), "href": elem.get_attribute("href")})

# links = list()
# for collect in collections:
#     if len(collect.split(" ")) == 1:
#         links.append("https://internationaldeliver.shop/collections/" + collect)
#     else:
#         link = collect.split(" ")
#         link = "-".join(link)
#         links.append("https://internationaldeliver.shop/collections/" + link + "/" + link)

newCollection = [i for i in collections ]


for link in collections: 
    driver.get(link["href"])
    products = driver.find_elements_by_class_name("grid-product__meta")
    
    try:
        pages = driver.find_elements_by_class_name("page")

        if len(pages) > 0:

           for page in range(len(pages)):
                if page == 0:
                    continue
                else:
                    count = page + 1
                    newCollection.append({"name": link["name"], "href": link["href"] + "?page=" + str(page)})
        else:
            print("pages length ", len(pages))    
    except:
        print("---- no pagination ")
    
collectionWithLinks = dict()

for collectionName in newCollection:
    collectionWithLinks[collectionName["name"]] = []

savingLinks = list()

for eachPage in newCollection:
    driver.get(eachPage["href"])
    collectionProducts = driver.find_elements_by_class_name("grid-product__meta")

    print(len(collectionProducts))
    for product in collectionProducts:
        savingLinks.append({"collection": eachPage["href"], "link": product.get_attribute("href") })
        try:
            collectionWithLinks[eachPage["name"]] = collectionWithLinks[eachPage["name"]].append(product.get_attribute("href"))
        except:
            collectionWithLinks[eachPage["name"]] = [product.get_attribute("href")]


print(savingLinks)
time.sleep(2)

driver.quit()
