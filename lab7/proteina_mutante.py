from protein import Proteina
import random
class ProteinaMutante(Proteina):
    def __init__(self):
        super().__init__()
        self.__mutacion = None

    def get_mutacion(self):
        return self.__mutacion
    

    def set_mutacion(self):
        muta = ["Sí","No"]
        ayuda = random.randint(0,1)
        mutacion = muta[ayuda]

        if isinstance(mutacion,str):
            self.__mutacion = mutacion
        else:
            print("Tipo de dato incorrecto")
