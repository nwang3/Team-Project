import requests
from bs4 import BeautifulSoup

url = "https://www.zillow.com/homedetails/61-Wayland-St-Boston-MA-02125/59106383_zpid/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

def find_element(soup, selector, attribute=None):
    try:
        if attribute:
            return soup.find(selector).get(attribute)
        return soup.find(selector).text
    except AttributeError:
        return "N/A"

try:
    price = find_element(soup, "span[data-test='property-card-price']")
except AttributeError:
    price = "N/A"

try:
    zip_code = find_element(soup, "span[itemprop='postalCode']")
except AttributeError:
    zip_code = "N/A"

details = soup.find("ul", {"class": "StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 eYPFID"})

try:
    beds = find_element(details, "li")
except AttributeError:
    beds = "N/A"

try:
    baths = find_element(details, "li", "text")
except AttributeError:
    baths = "N/A"

try:
    address = find_element(soup, "span[itemprop='addressLocality']")
    address_parts = address.split(", ")
    city = address_parts[0]
    state = address_parts[1] if len(address_parts) > 1 else "N/A"
except AttributeError:
    city = "N/A"
    state = "N/A"

print("Price:", price)
print("Zip Code:", zip_code) 
print("Beds:", beds)
print("Baths:", baths)
print("City:", city)  
print("State:", state)