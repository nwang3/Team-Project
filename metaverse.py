class RealEstateProperty:
    def __init__(self, address, price, bedrooms, bathrooms, status="For Sale"):
        self.address = address
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.status = status

    def display_info(self):
        print(f"Property Information:\nAddress: {self.address}\nPrice: ${self.price:,.2f}\nBedrooms: {self.bedrooms}\nBathrooms: {self.bathrooms}\nStatus: {self.status}")

class RealEstateAgent:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def display_properties(self):
        print(f"{self.name}'s Properties:")
        for property in self.properties:
            property.display_info()

class Buyer:
    def __init__(self, name, budget):
        self.name = name
        self.budget = budget

    def view_property(self, property):
        print(f"{self.name} is viewing the property at {property.address}.")
        property.display_info()

    def make_offer(self, property, offer_price):
        if offer_price >= property.price:
            print(f"{self.name} makes an offer of ${offer_price:,.2f} for the property at {property.address}. Offer accepted!")
            property.status = "Sold"
        else:
            print(f"{self.name}'s offer of ${offer_price:,.2f} for the property at {property.address} is too low. Offer rejected.")

# Example usage
property1 = RealEstateProperty("123 Main St", 500000, 3, 2.5)
property2 = RealEstateProperty("456 Oak Ave", 750000, 4, 3)

agent = RealEstateAgent("John Doe")
agent.add_property(property1)
agent.add_property(property2)

buyer = Buyer("Alice", 600000)
buyer.view_property(property1)
buyer.make_offer(property1, 550000)

agent.display_properties()
