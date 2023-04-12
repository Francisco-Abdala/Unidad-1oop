class AnalizadorProteico():
    def __init__(self):
        self.__lista = []

    def get_lista(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])

    def set_lista(self,parametro):
        self.__lista.append(parametro)

    def suma(self,parametro):
        for i in range(len(self.__lista)):
            if i == parametro:
                ayuda = self.__lista[parametro]
                suma_A = 0
                suma_V = 0
                suma_L = 0
                suma_I = 0
                suma_M = 0
                suma_F = 0
                for i in ayuda.get_secuencia():
                    if i == "A":
                        suma_A += 1
                    elif i == "V":
                        suma_V += 1
                    elif i == "L":
                        suma_L +=1
                    elif i == "I":
                        suma_I +=1
                    elif i == "M":
                        suma_M += 1
                    elif i == "F":
                        suma_F += 1
                diccionario = {"A": suma_A,"V":suma_V,"L":suma_L,"I":suma_I, "M": suma_M, "F": suma_F}
        help = diccionario.get("A") + diccionario.get("V") + diccionario.get("L") + diccionario.get("I") + diccionario.get("M") + diccionario.get("F")
        porcentaje = (help/len(ayuda.get_secuencia())) * 100
        
        print(f"El porcentaje de aminoacidos hidrofobos es: {porcentaje} %")


