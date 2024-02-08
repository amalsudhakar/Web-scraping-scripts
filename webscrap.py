import requests
from bs4 import BeautifulSoup
import re

url ="https://crinacle.com/rankings/iems/"

response =  requests.get(url)

if response.status_code == 200:
    print("linked accessed successfully")

    soup = BeautifulSoup(response.text , 'html.parser')

    table = soup.find('table')

    rows = table.find_all('tr')

    for row in rows[1:]:
        columns = row.find_all('td')
        rank = columns[0].text.strip()
        name = columns[2].text.strip()
        price_text = columns[3].text.strip()
        match = re.search(r'\d+(?=\s)', price_text) #extracting only the numbers, iqnoring other characters
        if match:
            price_numeric = float(match.group())
        else:
            try: 
                price_numeric = float(price_text) #if there is only numbers present in it
            except:    # noqa: E722
                price_numeric = 0 #if the vakue is discount
        if price_numeric < 100:
            print(f"{rank}\t\t{name}\t\t{price_numeric}")
else:
    print("failed to access url")