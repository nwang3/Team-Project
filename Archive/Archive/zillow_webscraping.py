import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.zillow.com/boston-ma/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-71.22958605957032%2C%22east%22%3A-70.8656639404297%2C%22south%22%3A42.17669701001186%2C%22north%22%3A42.44986970559557%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A44269%2C%22regionType%22%3A6%7D%5D%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
response = requests.get(url)
zillow = response.content

soup = BeautifulSoup(zillow, 'html.parser')

property_cards = soup.find_all('article', {'data-test': 'property-card'})

csv_file = open('listings.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Address', 'City', 'State', 'Price', 'Beds', 'Baths', 'Listed Date'])

for card in property_cards:
    address_elem = card.find('address', {'data-test': 'property-card-addr'})
    address = address_elem.text.strip() if address_elem else None

    city = card.find('address').text.split(',')[0]
    state = card.find('address').text.split(',')[1].strip() 
    price = card.find('span', {'data-test': 'property-card-price'}).text
    beds = card.find('li').text.split()[0]
    baths = card.find_all('li')[1].text.split()[0]
    listed_date = card.find('span', {'class': 'StyledPropertyCardBadge'}).text
    
    csv_writer.writerow([address, city, state, price, beds, baths, listed_date])
    
csv_file.close()