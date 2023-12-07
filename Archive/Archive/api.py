import requests

def get_listings(api_key, access_token, client_id, start_zg_listing_id=None, limit=None):
    api_url = "https://rentalsapi.zillowgroup.com/listings/v1/listingsForUser"

    
    params = {
        "accessToken": access_token,
        "clientId": client_id,
        "apiKey": api_key,
        "startZgListingId": start_zg_listing_id,
        "limit": limit
    }

    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        data = response.json()

        if data["status"] == "success":
            return data["payload"]
        else:
            print(f"API request failed with errors: {data['errors']}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None

if __name__ == "__main__":
    api_key = ""
    access_token = ""
    client_id = ""

    listings = get_listings(api_key, access_token, client_id, limit=5)

    if listings:
        print("Listings:")
        for i, listing in enumerate(listings, start=1):
            print(f"\nListing {i}:")
            print(f"Zillow Group Listing ID: {listing['zgListingId']}")
            print("Listing Address:")
            print(f"  Street: {listing['listingAddress']['street']}")
            print(f"  City: {listing['listingAddress']['city']}")
            print(f"  State: {listing['listingAddress']['state']}")
            print(f"  Zip Code: {listing['listingAddress']['zip']}")
            print(f"Listing Email: {listing['listingEmail']}")
            print(f"Listing Phone: {listing['listingPhone']}")
            print(f"Listing Start Date: {listing['listingStartDate']}")
            print(f"Zillow URL: {listing['zillowUrl']}")
            print(f"HotPads URL: {listing['hotpadsUrl']}")
            print(f"Trulia URL: {listing['truliaUrl']}")
    else:
        print("No listings found.")
