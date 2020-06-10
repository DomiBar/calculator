import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
variable1 = input("Podaj składnik 1. ")
try:
    float(variable1)
    res=True
except:
    print("Podany składnik nie jest liczbą")
    exit()

variable2 = input("Podaj składnik 2. ")
try:
    float(variable2)
    res=True
except:
    print("Podany składnik nie jest liczbą")
    exit()

variable1=float(variable1)
variable1=float(variable2)

if operation==1:
    logging.debug(f"Dodaję {variable1} i {variable2}")
    print(f"Wynik to {variable1+variable2}")
elif operation==2:
    logging.debug(f"Odejmuję {variable2} od {variable1}")
    print(f"Wynik to {variable1-variable2}")
elif operation==3:
    logging.debug(f"Mnożę {variable1} i {variable2}")
    print(f"Wynik to {variable1*variable2}")
elif operation==4:
    logging.debug(f"Dzielę {variable1} przez {variable2}")
    print(f"Wynik to {variable1/variable2}")
