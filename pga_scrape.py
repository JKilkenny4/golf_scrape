import requests
from bs4 import BeautifulSoup

url = 'https://www.espn.com/golf/leaderboard'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#t = soup.find('h1', class_ = 'chakra-text css-axbyz4').text
leader_table = soup.find('table', class_ = 'Table Table--align-right Full__Table')
for player in leader_table.find_all('tbody'):
    rows = player.find_all('tr')
    for row in rows:
        pos = row.find('td', class_ = 'tl Table__TD').text
        name = row.find('td', class_ = 'tl plyr Table__TD').text
        f_score = row.find_all('td', class_ = 'Table__TD')[3].text
        r1_score = row.find_all('td', class_ = 'Table__TD')[4].text,
        r2_score = row.find_all('td', class_ = 'Table__TD')[5].text,
        r3_score = row.find_all('td', class_ = 'Table__TD')[6].text,
        r4_score = row.find_all('td', class_ = 'Table__TD')[7].text
        print(pos, name, f_score, r1_score, r2_score, r3_score, r4_score)