from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1,20):
    
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&xpid=DlNNJmH6ckBXM&crid=2XES8RUBB5SBD&qid=1781588880&sprefix=laptop%2Caps%2C294&ref=sr_pg_2")
    elem = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    #print(elem.text)
    print(f"{len(elem)} items found")
    for elems in elem:
        data = elems.get_attribute("outerHTML")
        with open(f"data/{query}-{file}.html", "w", encoding="utf-8") as f:
            f.write(data)
            file+=1
            
time.sleep(6)
driver.close()