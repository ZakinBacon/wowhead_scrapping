from bs4 import BeautifulSoup
import requests
from lxml import etree
import pandas as pd

headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

response = requests.get("https://www.wowhead.com/guide/classes/paladin/retribution/bis-gear", headers=headers)
wowhead_webpage = response.content

# Creating our Soup
soup = BeautifulSoup(wowhead_webpage, "html.parser")


dfs = pd.read_html(wowhead_webpage)


raid_bis = dfs[3]
print(raid_bis)

print(raid_bis.iloc[1])


# all_neck = soup.select("table tr")#soup.find_all(name="tr")
# print(all_neck)
