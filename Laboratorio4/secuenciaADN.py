class SecuenciaADN():
    def __init__(self,parametro1,parametro2):
        self.__longitud = parametro1
        self.__caracter = parametro2
        self.__inversa = None
    def get_longitud(self):
        return self.__longitud
    def get_caracter(self):
        return self.__caracter
    
    def set_cadena_inversa(self):
        reverso = ""
        comp = {"A": "T", "T":"A","C":"G","G":"C"}
        longitud = len(self.__caracter)
        for i in range (longitud):
            ayuda = self.__caracter[longitud - 1 - i]
            reverso = reverso + comp.get(ayuda,ayuda)
        print(f"La cadena complementaria de la cadena inversa es: {reverso}" )
        if isinstance(reverso,str):
            self.__inversa = reverso

    def get_reverso(self):
        return self.__inversa
    
    def contar_nucleotidos(self):
        suma_a = 0
        suma_t = 0
        suma_c = 0
        suma_g = 0
        for i in self.__caracter:
            if i == "A":
                suma_a += 1
            elif i == "T":
                suma_t += 1
            elif i == "C":
                suma_c +=1
            elif i == "G":
                suma_g +=1
        diccionario = {"A": suma_a,"T":suma_t,"C":suma_c,"G":suma_g}
        return diccionario
    

    def peso_molecular(self):
        dic = self.contar_nucleotidos()
        print("Cantidad de A: ", dic.get("A") ,"cantidad de T :" , dic.get("T") ,"cantidad de C :", dic.get("C") ,"cantidad de G: ", dic.get("G"))
        masa = (dic.get("A")*313.21) + (dic.get("T")*304.2 ) + (dic.get("C")*298.18) + (dic.get("G")*329.21)
        print(f"El peso molecular de la cadena es: {masa} Kg/mol")
    
    def encontrar_patron(self,parametro1):
        cadena = self.__caracter
        posicion = []
        while cadena.find(parametro1) != -1:
            posicion.append(cadena.find(parametro1) + 1)
            cadena = cadena.replace(parametro1,parametro1.lower(), 1)
        print(f"Se encontró el patrón en las siguientes posiciones: {posicion}")

            

