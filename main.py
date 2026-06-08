+94751621827 phonenumbers
from test import selvi

from phonenumbers import geocoder
ch_number = +94751621827.parse(selvi,"ch")
print(geocoder.description_for_number(ch_number,"en"))

from phonenumbers import carrier
service_number = +94751621827.parse(selvi ,"RO")
print(carrier.name_for_number(ch_number ,"en"))