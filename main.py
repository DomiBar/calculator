import logging
import operations
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filename="logfile.log")

components = []

res = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
try:
    variable1 = float(input("Podaj składnik 1. "))
except:
    print("Podany składnik nie jest liczbą")
    exit()

try:
    variable2 = float(input("Podaj składnik 2. "))
except:
    print("Podany składnik nie jest liczbą")
    exit()

if res == 1 or res == 3:
    components = operations.take_components(variable1, variable2)

if res == 1:
    logging.debug(f"Dodaję następujące liczby {components}")
    print(f"Wynik to {operations.add(components)}")
elif res == 2:
    logging.debug(f"Odejmuję {variable2} od {variable1}")
    print(f"Wynik to {operations.subtract(variable1,variable2)}")
elif res == 3:
    logging.debug(f"Mnożę następujące liczby {components}")
    print(f"Wynik to {operations.multiply(components)}")
elif res == 4:
    logging.debug(f"Dzielę {variable1} przez {variable2}")
    print(f"Wynik to {operations.divide(variable1,variable2)}")
