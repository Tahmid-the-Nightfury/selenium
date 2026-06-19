from bs4 import BeautifulSoup
import os
import pandas as pd


data = {'tittle': [], 'price':[], 'link':[]}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text()
        l = soup.find("a", class_="a-link-normal")
        link = "https://amazon.in/"+l['href']
        p = soup.find("span", class_="a-offscreen")
        price = p.get_text()+"tk"
        data['tittle'].append(title)
        data['link'].append(link)
        data['price'].append(price)
        
    except Exception as e:
        print(e)
        
df = pd.DataFrame(data=data)
df.to_csv("data.csv")