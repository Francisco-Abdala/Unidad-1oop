from protein import Proteina
class SecuenciaProteica():
    def __init__(self):
        self.__listado = []

    def set_lista(self,parametro):
        self.__listado.append(parametro)

    def get_lista(self):
        for i in range (len(self.__listado)):
            print(self.__listado[i].get_nombre())

    def mostrar_secuencia(self,parametro):
        for i in range(len(self.__listado)):
            if i == parametro:
                print(self.__listado[i].get_secuencia())
