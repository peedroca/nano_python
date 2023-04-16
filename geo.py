from pygeocoder import Geocoder

# Connection on Google API and get cords from address
address = '1222, Lins de Vasconselos, Sao Paulo, SP'
print(Geocoder('key').geocode(address))
