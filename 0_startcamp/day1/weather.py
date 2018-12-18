from darksky import forecast

multicampus = forecast('a11e9488156cceaddf3805cad9ea8cb4', 37.501554, 127.03966)

print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])


#import requests

#url = 'http://api.darksky.net/forecast/ '

#res = request.get(url)
#data = res.json()
#
