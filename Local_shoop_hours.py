# Script to store five local shop names and their opening hours in Grimsby, UK
shop_hours = {
    "Grimsby Fish Market": "8:00 AM - 5:00 PM",
    "Freshfields Farm Shop": "9:00 AM - 6:00 PM",
    "Tesco Grimsby": "7:00 AM - 10:00 PM",
    "Greggs Grimsby": "6:30 AM - 6:00 PM",
    "Wilko Grimsby": "8:00 AM - 8:00 PM"
}

# Display the shop names and their opening hours
print("Local Shops in Grimsby and Their Opening Hours:")
for shop, hours in shop_hours.items():
    print(f"{shop}: {hours}")