import phonenumbers
from phonenumbers import geocoder
phone_numbers1 = phonenumbers.parse("+917876832283")
phone_numbers2 = phonenumbers.parse("+919857129221")
print(geocoder.description_for_number(phone_numbers1 ,"en"))
print(geocoder.description_for_number(phone_numbers2 ,"en"))