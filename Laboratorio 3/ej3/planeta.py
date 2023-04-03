class Planeta():
    def __init__(self):
        self.__masa = None
        self.__densidad = None
        self.__diametro = None
        self.__identificador = None
        self.__nombre = None

    def get_nombre(self):
        return self.__nombre
    
    def get_masa(self):
        return self.__masa

    def get_densidad(self):
        return self.__densidad
    
    def get_diametro(self):
        return self.__diametro
    
    def get_identificador(self):
        return self.__identificador
    
    def set_masa(self,ingreso):
        if isinstance(ingreso, int):
            self.__masa = ingreso
        else:
            print("Tipo de dato incorrecto")
            
    def set_densidad(self,ingreso):
        if isinstance(ingreso,int):
            self.__densidad = ingreso
        else:
            print("Tipo de dato incorrecto")
    def set_diametro(self,ingreso):
        if isinstance(ingreso, int):
            self.__diametro = ingreso
        else:
            print("Tipo de dato incorrecto")

    def set_identificador(self,ingreso):
        if isinstance(ingreso, str):
            self.__identificador = ingreso
        else:
            print("Debe de tener al menos un número")
    
    def set_nombre(self,ingreso):
        if isinstance(ingreso,str):
            self.__nombre = ingreso
        else:
            print("Tipo de dato incorrecto")