from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=2XES8RUBB5SBD&sprefix=laptop%2Caps%2C294&ref=nb_sb_noss_2")
elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")
#print(elem.text)
print(f"{len(elem)} items found")
for elems in elem:
    print(elems.text)
time.sleep(6)
driver.close()