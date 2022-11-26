import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
print("Please make sure that you have an active Internet Connection right now. "
      "Otherwise you will be unable to get the location coordinates. You will only get the Service Provider and "
      "Country name\n")


number = input("Enter the Phone no. with country code: ")
pepnumber = phonenumbers.parse(number)

location = geocoder.description_for_number(pepnumber, "en")
print("The location for this Number is: ", end="")
print(location)

service_pro = phonenumbers.parse(number)
print("Service Provider is: ", end="")
print(carrier.name_for_number(service_pro, "en"))

key = '156511124bac42c0af64c0655fca39b2'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print("Locations Co-ordinates are:", end="")
print(lat, lng)
