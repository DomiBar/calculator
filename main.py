import logging
import operations
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(message)s', filename="logfile.log")

res = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

components = operations.take_components(res)

if res == 1:
    logging.debug(f"Dodaję następujące liczby {components}")
    print(f"Wynik to {operations.add(components)}")
elif res == 2:
    logging.debug(f"Odejmuję {components[1]} od {components[0]}")
    print(f"Wynik to {operations.subtract(components)}")
elif res == 3:
    logging.debug(f"Mnożę następujące liczby {components}")
    print(f"Wynik to {operations.multiply(components)}")
elif res == 4:
    logging.debug(f"Dzielę {components[0]} przez {components[1]}")
    print(f"Wynik to {operations.divide(components)}")
