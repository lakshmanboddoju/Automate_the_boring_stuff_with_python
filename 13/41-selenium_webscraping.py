#! python3

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

element = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(23) > li:nth-child(1) > a:nth-child(1)')
elements = browser.find_elements_by_css_selector('p')

browser.get('https://google.com')
searchElem = browser.find_element_by_css_selector('.gLFyf')
searchElem.send_keys('Lakshman Boddoju')
searchElem.submit()

browser.back()
browser.forward()
browser.refresh()

browser.quit()

# Again

browser = webdriver.Firefox()
browser.get('https://automatetheboringstuff.com')

elementP = browser.find_element_by_css_selector('.main > div:nth-child(1) > p:nth-child(9)')
elementPText = elementP.text

print(elementPText)

elementAll = browser.find_element_by_css_selector('html')
elementAllText = elementAll.text

browser.quit()
