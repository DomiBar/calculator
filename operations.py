import logging


def add(components):
    result = 0
    for i in range(len(components)):
        result += components[i]
    return result


def subtract(components):
    return components[0]-components[1]


def multiply(components):
    result = 1
    for i in range(len(components)):
        result = result * components[i]
    return result


def divide(components):
    return components[0]/components[1]


def take_components(res):
    components=[]

    for i in range(2):
        component = input(f"Podaj składnik {len(components)+1}: ")
        try:
            components.append(float(component))
        except:
            print("Podany składnik nie jest liczbą")
            exit()

    if res==1 or res==3:
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
