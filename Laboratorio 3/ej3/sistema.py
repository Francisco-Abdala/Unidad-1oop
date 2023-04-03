class Sistema():
    def __init__(self):
        self.__sistema = []
    
    def set_sistema(self,x):
        self.__sistema.append(x)
    def get_sistema(self):
        return self.__sistema
    def mostrar_sistema(self):
        for i in range (len(self.__sistema)):
            print(self.__sistema[i].get_nombre())
    
    def mostrar_atributos(self,ayuda):
        for i in range(len(self.__sistema)):
            if self.__sistema[i].get_nombre().lower() == ayuda.lower():
                print(f"Nombre: {self.__sistema[i].get_nombre()}")
                print(f"Masa: {self.__sistema[i].get_masa()} Kg")
                print(f"Densidad: {self.__sistema[i].get_densidad()} g/cm cúbico")
                print(f"Diametro: {self.__sistema[i].get_diametro()} Km")       
                print(f"Identificador: {self.__sistema[i].get_identificador()}")         