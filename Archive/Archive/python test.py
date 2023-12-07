from lxml import html
import requests
import unicodecsv as csv

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

def get_user_input():
    zipcode = input("Enter the ZIP code: ")
    return zipcode

def parse(zipcode, filter=None):
    if filter == "newest":
        url = f"https://www.zillow.com/homes/for_sale/{zipcode}/0_singlestory/days_sort"
    elif filter == "cheapest":
        url = f"https://www.zillow.com/homes/for_sale/{zipcode}/0_singlestory/pricea_sort/"
    else:
        url = f"https://www.zillow.com/homes/for_sale/{zipcode}_rb/?fromHomePage=true&shouldFireSellPageImplicitClaimGA=false&fromHomePageTab=buy"

    for i in range(5):
        try:
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'accept-encoding': 'gzip, deflate, sdch, br',
                'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
                'cache-control': 'max-age=0',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            print(response.status_code)

            parser = html.fromstring(response.text)
            search_results = parser.xpath("//div[@id='search-results']//article")
            properties_list = []

            for properties in search_results:
                raw_address = properties.xpath(".//span[@itemprop='address']//span[@itemprop='streetAddress']//text()")
                raw_city = properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressLocality']//text()")
                raw_state = properties.xpath(".//span[@itemprop='address']//span[@itemprop='addressRegion']//text()")
                raw_postal_code = properties.xpath(".//span[@itemprop='address']//span[@itemprop='postalCode']//text()")
                raw_price = properties.xpath(".//span[@class='zsg-photo-card-price']//text()")
                raw_info = properties.xpath(".//span[@class='zsg-photo-card-info']//text()")
                raw_broker_name = properties.xpath(".//span[@class='zsg-photo-card-broker-name']//text()")
                url = properties.xpath(".//a[contains(@class,'overlay-link')]/@href")
                raw_title = properties.xpath(".//h4//text()")

                address = ' '.join(' '.join(raw_address).split()) if raw_address else None
                city = ''.join(raw_city).strip() if raw_city else None
                state = ''.join(raw_state).strip() if raw_state else None
                postal_code = ''.join(raw_postal_code).strip() if raw_postal_code else None
                price = ''.join(raw_price).strip() if raw_price else None
                info = ' '.join(' '.join(raw_info).split()).replace(u"\xb7", ',')
                broker = ''.join(raw_broker_name).strip() if raw_broker_name else None
                title = ''.join(raw_title) if raw_title else None
                property_url = "https://www.zillow.com" + url[0] if url else None
                is_for_sale = properties.xpath('.//span[@class="zsg-icon-for-sale"]')
                properties_data = {
                    'title': title,
                    'address': address,
                    'city': city,
                    'state': state,
                    'postal_code': postal_code,
                    'price': price,
                    'facts and features': info,
                    'real estate provider': broker,
                    'url': property_url
                }

                if is_for_sale:
                    properties_list.append(properties_data)

            return properties_list
        except Exception as e:
            print("Failed to process the page", url, e)

if __name__ == "__main__":
    zipcode = get_user_input()
    sort = input("Enter the sort order (newest/cheapest): ").lower()

    print(f"Fetching data for {zipcode}")
    scraped_data = parse(zipcode, sort)

    if scraped_data:
        print("\nProperty Data:")
        for i, property_data in enumerate(scraped_data, start=1):
            print(f"\nProperty {i}:")
            for key, value in property_data.items():
                print(f"{key}: {value}")
    else:
        print("No properties found.")
