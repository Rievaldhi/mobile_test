import phonenumbers
from cek_number import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

# ch_no = phonenumbers.parse(number, 'CH')
# print(geocoder.description_for_number(ch_no, 'en'))

# service_no = phonenumbers.parse(number, 'RO')
# print(carrier.name_for_number(service_no, 'en'))

no =  phonenumbers.parse(number)
loc = geocoder.description_for_number(no, 'en')
print(loc)

geocoder = OpenCageGeocode(Key)