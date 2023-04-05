import random
class Secuenciador():
    def __init__(self):
        self.__info = None
        self.__nombre = None

    def set_secuencia(self):
        bases = ["A","T","C","G"]
        temp = ""
        while True:
            longitud = input("Ingrese la longitud de su cadena: ")
            if longitud.isnumeric():
                longitud_int = int(longitud)
                break
            else:
                print("Ingrese un dato numerico")
                continue
        for i in range(0,longitud_int):
            rng = random.randint(0,3)
            temp += bases[rng]
        
        if isinstance(temp,str):
            self.__info = temp
        else:
            print("Tipo de dato incorrecto")

    def get_informacion(self):
        return self.__info

    def set_nombre(self):
        while True:
            dato = input("Ingrese el nombre de su cadena: ")
            if dato.isnumeric():
                print("Tipo de dato incorrecto")
                continue
            else:
                break
        if isinstance(dato,str):
            self.__nombre = dato
        else:
            print("Tipo de dato incorrecto")
    def get_nombre(self):
        return self.__nombre
    
    def get_longitud(self):
        return len(self.__info)
