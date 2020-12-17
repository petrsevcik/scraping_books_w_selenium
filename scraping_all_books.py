from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import re
import os
#scraping books from http://books.toscrape.com. inspiration and big help from https://towardsdatascience.com/web-scraping-e-commerce-website-using-selenium-1088131c8541


PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)
#driver.get("http://books.toscrape.com/catalogue/page-1.html")
driver.get("http://books.toscrape.com/catalogue/category/books_1/page-1.html")
#links to the books on the first page
incategory = driver.find_elements_by_class_name("product_pod")
links = []
for i in range(len(incategory)):
    item = incategory[i]
    a = item.find_element_by_tag_name("h3").find_element_by_tag_name("a").get_property("href")
    links.append(a)
#getting texts from each book`s page
texts = []
for link in links:
    driver.get(url=link)
    description = driver.find_elements_by_tag_name("p")[3]
    r = description.text
    texts.append(r)

#write it to txt file
file = open("texts.txt","a")
for text in texts:
    file.write(text)
file.close()

time.sleep(5)
driver.close()