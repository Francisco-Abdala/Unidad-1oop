#Clase que se trabajará
class Vacuna():
    def __init__(self):
        self.__nombre = None
        self.__lab = None
        self.__efectos = []

    def get_nombre(self):
        return self.__nombre
    
    #Comprueba que lo ingresado sea un str
    def set_nombre_vacuna(self,nombre):
        if isinstance(nombre,str):
            self.__nombre = nombre
        else:
            print("Tipo de dato incorrecto")
            
    def get_lab(self):
        return self.__lab
    
    #Comprueba que lo ingresado sea un str
    def set_lab(self,lab):
        if isinstance(lab, str):
            self.__lab = lab
        else: 
            print("Tipo de dato incorrecto")
    def get_efectos(self):
        return self.__efectos
    def set_agrega_efecto_secundario(self,algo):
        self.__efectos.append(algo)


    #Imprime en pantalla los efectos secundarios del medicamento escogido
    def mostrar_efectos(self):
        for i in range (len(self.__efectos)):
            print(self.__efectos[i])