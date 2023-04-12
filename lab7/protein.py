import random
 #pasar parametros
class Proteina():
    def __init__(self):
        self.__nombre = None
        self.__descrpcion = None
        self.__secuencia = None
    
    def get_nombre(self):
        return self.__nombre
    

    def get_descripcion(self):
        return self.__descrpcion
    

    def get_secuencia(self):
        return self.__secuencia
    

    def set_nombre(self,parametro):
        if isinstance(parametro, str):
            self.__nombre = parametro
        else:
            print("Tipo de dato incorrecto")


    def set_descripcion(self,parametro):
        if isinstance(parametro, str):
            self.__descrpcion = parametro
        else:
            print("Tipo de dato incorrecto")
    
    def set_secuencia(self):
        dic = {1: "A", 2: "R", 3: "N",4:"D", 5:"C", 6:"Q", 7:"E", 
               8:"G", 9:"H", 10:"I", 11:"L", 12:"K", 13:"M", 14:"F", 15:"P", 16:"S",
               17:"T", 18:"W", 19:"Y", 20:"V"}
        while True:
            temp = ""
            longitud = input("Ingrese la longitud de su proteina: ")
            if longitud.isnumeric():
                longitud_int = int(longitud)
                break
            else:
                print("Tipo de dato incorrecto")
                continue
        for i in range(0,longitud_int):
            rng = random.randint(1,20)
            temp += dic[rng]
        if isinstance(temp,str):
            self.__secuencia = temp
        else:
            print("Tipo de dato incorrecto")
