import logging


def add(components):
    result = 0
    for i in range(len(components)):
        result += components[i]
    return result


def subtract(variable1, variable2):
    return variable1-variable2


def multiply(components):
    result = 1
    for i in range(len(components)):
        result = result * components[i]
    return result


def divide(variable1, variable2):
    return variable1/variable2


def take_components(variable1, variable2):
    components = [variable1, variable2]
    res = input("Czy dodać kolejny składnik [y]")
    while res == 'y':
        component = input(f"Podaj składnik {len(components)+1}: ")
        try:
            components.append(float(component))
        except:
            print("Podany składnik nie jest liczbą")
            exit()
        res = input("Czy dodać kolejny składnik [y]")
    return components
