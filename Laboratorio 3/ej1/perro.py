class Perro():
    def __init__(self):
        self.__nombre = None
        self.__agua = 0
        self.__pasear = False

    def para(self):
        self.__pasear = False

    def get_pasear(self):
        if self.__pasear:
            print("Puede pasear")
            return True
        else:
            print("NO puede pasear")
            return False

    def pasear(self):
        if self.__agua < 4:
            self.__pasear = True

    def tomar_agua(self):
        if not self.__pasear:
            self.__agua = 0
        else:
            print("No puede tomar agua")

    def get_hora_toma_agua(self):
        return self.__agua

    def set_hora_toma_agua(self, tiempo):
        if isinstance(tiempo, int):
            self.__agua = self.__agua + tiempo

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es String")
