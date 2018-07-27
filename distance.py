import requests
import sys
import urllib.request
from math import *
import time
from geopy.geocoders import Nominatim

# gn = geocoders.GeoNames(username = "")
geolocator = Nominatim()

def greatCircleDistance(lat1, lon1, lat2, lon2):
	def haversin(x):
		return sin(x/2)**2 
	return 2 * asin(sqrt(haversin(lat2-lat1) + cos(lat1) * cos(lat2) * haversin(lon2-lon1))) * 6371 * 0.02

d = {}

#  mydict = {'carl':40, 'alan':2, 'bob':1, 'danny':3}

# for key, value in sorted(mydict.items(), key=lambda kv: (-kv[1], kv[0])):
#     print("{}: {}".format(key, value))

addr1 = ""
city = ""
with open('textfiles/location1.txt', 'r') as file1:
	lines = file1.readlines()
	addr1 = lines[0]
	city = lines[1]
response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}'.format(addr1))
resp_json_payload = response.json()
lat1 = resp_json_payload['results'][0]['geometry']['location']['lat'] 
long1 = resp_json_payload['results'][0]['geometry']['location']['lng']

# location = geolocator.geocode("addr1")
# print(location.raw)

# print(addr1)
# lat1 = gn.geocode(addr1).latitude
# long1 = gn.geocode(addr1).longitude
print(str(lat1) + "," + str(long1))

last = 0
current = 0
done = False

while done != True:
	time.sleep(2)
	try:
		with open('textfiles/namelist.txt', 'r') as file2:
			lines = file2.readlines()
			for i in range (last, len(lines)):
				current = i
				name = lines[i]
				addr2 = urllib.request.quote(name, city)
				response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={}'.format(addr2))
				resp_json_payload = response.json()
				lat2 = resp_json_payload['results'][0]['geometry']['location']['lat'] 
				long2 = resp_json_payload['results'][0]['geometry']['location']['lng']
				# print(str(lat2) + "," + str(long2))
				dist = greatCircleDistance(lat1, long1, lat2, long2)
				d[name] = dist

				if i >= len(lines) - 1:
					done = True

	except:
		e = sys.exc_info()[0]
		print("Failed... trying again: " + str(e))
		last = current

for key, value in sorted(d.items(), key=lambda kv: (-kv[1], kv[0])):
    print("{}: {}".format(key, value))

# print(str(lat1) + "," + str(long1))
# mbox.showinfo('my app','Info: ' + str(resp_json_payload['results'][0]['geometry']['location']))