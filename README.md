##  Geolocation Script with Geopy
#  Overview
This Python program allows users to input a city name and retrieve its geographical location using the geopy library. It outputs the details of the location, including latitude, longitude, and other relevant information.

##  Requirements
1.  Python 3.x
2.  geopy library

##  Installation
To install the required library, use pip:

##  cmd
pip install geopy


Usage
1.  Clone this repository or copy the script to your local machine.
2.  Open a terminal or command prompt and navigate to the directory where the script is located.
3.  Run the script using Python:  "python geolocation.py"

When prompted, enter the name of the city you want to locate.
#  Example
  Enter City Name: New York
  Location(location='New York, New York, United States', latitude=40.712776, longitude=-74.005974, ...)
  
##  Error Handling
  If the city name entered does not return any location data, the script will display a message indicating that the location was not found.
