from selenium import webdriver

URL = input("URL:\n")

link = URL

browser = webdriver.chrome()
browser.get(URL)

browser.find_element_by_xpath().click()
