import logging
import operations
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

components=[]

operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
try:
    variable1=float(input("Podaj składnik 1. "))
except:
    print("Podany składnik nie jest liczbą")
    exit()

try:
    variable2=float(input("Podaj składnik 2. "))
except:
    print("Podany składnik nie jest liczbą")
    exit()

components=[variable1,variable2]
if operation==1:
    operations.take_components(components)
    logging.debug(f"Dodaję następujące liczby {components}")
    print(f"Wynik to {operations.add(components)}")
elif operation==2:
    logging.debug(f"Odejmuję {variable2} od {variable1}")
    print(f"Wynik to {variable1-variable2}")
elif operation==3:
    operations.take_components(components)
    logging.debug(f"Mnożę następujące liczby {components}")
    print(f"Wynik to {operations.multiply(components)}")
elif operation==4:
    logging.debug(f"Dzielę {variable1} przez {variable2}")
    print(f"Wynik to {variable1/variable2}")