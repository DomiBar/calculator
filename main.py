operation = int(input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
variable1=float(input("Podaj składnik 1. "))
variable2=float(input("Podaj składnik 2. "))

if operation==1:
    print(f"Dodaję {variable1} i {variable2}")
    print(f"Wynik to {variable1+variable2}")
elif operation==2:
    print(f"Odejmuję {variable2} od {variable1}")
    print(f"Wynik to {variable1-variable2}")
elif operation==3:
    print(f"Mnożę {variable1} i {variable2}")
    print(f"Wynik to {variable1*variable2}")
elif operation==4:
    print(f"Dzielę {variable1} przez {variable2}")
    print(f"Wynik to {variable1/variable2}")
