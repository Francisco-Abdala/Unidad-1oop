from protein import Proteina
import random
class ProteinaEstructural(Proteina):
    def __init__(self):
        super().__init__()
        self.__tipo = None
    
    def get_tipo(self):
        return self.__tipo
    #pasar parametro

    def set_tipo(self):
        tipos = ["Globular","Fibrosa"]
        ayuda = random.randint(0,1)
        tipo = tipos[ayuda]
        if isinstance(tipo,str):
            self.__tipo = tipo
        else:
            print("Tipo de dato incorrecto")
