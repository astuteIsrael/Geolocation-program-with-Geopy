# pip install geopy

from geopy.geocoders import Nominatim

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

place = input("Enter City Name: ")

# Get the location
location = geolocator.geocode(place)

# Print the location details
if location:
    print(location)
else:
    print("Location not found.")
