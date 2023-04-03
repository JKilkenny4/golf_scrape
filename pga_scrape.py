import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.com/golf/leaderboard'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#t = soup.find('h1', class_ = 'chakra-text css-axbyz4').text
parsed_header = soup.find_all('table')[0].find('tr')
header = []
for i in parsed_header:
    header.append(i.get_text())

parsed_table = soup.find_all('table')[0].find_all('tr')[1:]
data = []
for rows in parsed_table:
    init_df = []
    for row in rows:
        init_df.append(row.get_text())
    data.append(init_df)

df = pd.DataFrame(data = data, columns=header).iloc[:,1:]

print(df)

