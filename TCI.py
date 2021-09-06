import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Ingresa numero de telefono: ")
mobileNo = phonenumbers.parse(mobileNo)

timezn = timezone.time_zones_for_number(mobileNo)
print("El pais del numero es: " + str(timezn))

NombreNum = carrier.name_for_number(mobileNo, "es")
if NombreNum == "":
    print("El nombre del  telefono es: Nombre no valido")
else:
    print("El nombre del numero es: " + str(NombreNum))


Geocoder = geocoder.description_for_number(mobileNo, "es")
print("El zona del numero es: " + str(Geocoder))

ValidNum = phonenumbers.is_valid_number(mobileNo)
if ValidNum == True:
    print("El numero es: Valido")
else:
    print("El numero es: No valido")

PossibleNum = phonenumbers.is_possible_number(mobileNo)
if PossibleNum == True:
    print("El numero es verdadero")
else:
    print("El numero no es verdadero")
