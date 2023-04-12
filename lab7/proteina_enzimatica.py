from protein import Proteina

class ProteinaEnzimatica(Proteina):
    def __init__(self):
        super().__init__()
        self.__substrato = None

    def get_substrato(self):
        return self.__substrato
    
    def set_substrato(self,parametro):
        if isinstance(parametro,str):
            self.__substrato = parametro
        else:
            print("Tipo de dato incorrecto")