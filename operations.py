import logging

def add(components):
    result=0
    for i in range(len(components)):
        result += components[i]
    return result

def multiply(components):
    result=1
    for i in range(len(components)):
        result = result * components[i]
    return result

def take_components(components):
    counter=3
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
