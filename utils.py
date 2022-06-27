import requests
from bs4 import BeautifulSoup

# get the html from a link
response = requests.get('https://www.twitch.tv/paymoneywubby')
soup = BeautifulSoup(response.text, 'html.parser')

with open('test.html', 'w') as f:
    f.write(soup.prettify())
