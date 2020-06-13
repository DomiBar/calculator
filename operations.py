import logging

def add(variable1,variable2):
    components=[variable1,variable2]
    counter=3
    result=0
    res=input("Czy dodać kolejny składnik [y]")
    while res == 'y':
        component=input(f"Podaj składnik {counter}: ")
        try:
            components.append(float(component))
        except:
            print("Podany składnik nie jest liczbą")
            exit()
        counter+=1
        res=input("Czy dodać kolejny składnik [y]")
    for i in range(len(components)):
        result += components[i]
    logging.debug(f"Dodaję następujące liczby {components}")
    print(f"Wynik to {result}")

def multiply(variable1,variable2):
    components=[variable1,variable2]
    counter=3
    result=1
    res=input("Czy pomnożyć kolejny składnik [y]")
    while res == 'y':
        component=input(f"Podaj składnik {counter}: ")
        try:
            components.append(float(component))
        except:
            print("Podany składnik nie jest liczbą")
            exit()
        counter+=1
        res=input("Czy pomnożyć kolejny składnik [y]")
    for i in range(len(components)):
        result = result * components[i]
    logging.debug(f"Mnożę następujące liczby {components}")
    print(f"Wynik to {result}")
