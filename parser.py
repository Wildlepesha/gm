import selenium
import logging
import time
from selenium import webdriver

driver = webdriver.Chrome()

time.sleep(5)

driver.get("https://otzovik.com/reviews/bank_sovkombank_russia/?order=date_desc")
time.sleep(5)


textarea = driver.find_element_by_css_selector("#content > div > div > div > div > div:nth-child(6) > div.ukQr0TpYvPcgNhJnCo7t2azm_Ms1a7QNP > div.pager > a.pager-item.next.tooltip-top")
textarea.click()
time.sleep(5)

time.sleep(5)
f = open('src.html', 'w', encoding='UTF-8')
src = driver.page_source
f.write(src)

driver.quit()

