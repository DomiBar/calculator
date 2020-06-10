import logging

def add(variable1,variable2):
    res=None
    components=[variable1,variable2]
    i=3
    result=0
    res=input("Czy dodać kolejny składnik [y]")
    while res == 'y':
        component=input(f"Podaj składnik {i}: ")
        try:
            float(component)
            res=True
        except:
            print("Podany składnik nie jest liczbą")
            exit()
        components.append(float(component))
        i+=1
        res=input("Czy dodać kolejny składnik [Y]")
    for i in range(len(components)):
        result += components[i]
    logging.debug(f"Dodaję następujące liczby {components}")
    print(f"Wynik to {result}")

def multiply(variable1,variable2):
    res=None
    components=[variable1,variable2]
    i=3
    result=1
    res=input("Czy pomnożyć kolejny składnik [y]")
    while res == 'y':
        component=input(f"Podaj składnik {i}: ")
        try:
            float(component)
            res=True
        except:
            print("Podany składnik nie jest liczbą")
            exit()
        components.append(float(component))
        i+=1
        res=input("Czy pomnożyć kolejny składnik [Y]")
    for i in range(len(components)):
        result = result * components[i]
    logging.debug(f"Mnożę następujące liczby {components}")
    print(f"Wynik to {result}")
