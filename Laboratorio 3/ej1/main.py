from time import sleep
from perro import Perro

def main():
    while True:
        escoge_perro = input("¿De qué perro desea obtener información? (1) para toby, (2) para cachupin: ")
        if escoge_perro.isnumeric():
            escoge_perro_int = int(escoge_perro)
        else:
            print("Tipo de dato incorrecto")
            break
        toby = Perro()
        cachupin = Perro()
        toby.set_nombre("Toby")
        cachupin.set_nombre("Cachupin")
        while escoge_perro_int == 1:
            for i in range(1, 5):
                toby.set_hora_toma_agua(1)
                sleep(1)
                print(toby.get_hora_toma_agua())
            toby.tomar_agua()
            print(toby.get_hora_toma_agua())
            print(toby.get_nombre(), " puede pasear")
            toby.pasear()
            if toby.get_pasear():
                print(toby.get_nombre(), " pasea")
            toby.set_hora_toma_agua(1)
            toby.tomar_agua()
            print(toby.get_hora_toma_agua())

            toby.para()
            toby.set_hora_toma_agua(1)
            toby.tomar_agua()
            print(toby.get_hora_toma_agua())

            break
            break
        while escoge_perro_int == 2:
            for i in range(1,7):
                cachupin.set_hora_toma_agua(2)
                sleep(1)
                print(cachupin.get_hora_toma_agua())
            cachupin.tomar_agua()
            print(cachupin.get_hora_toma_agua())
            if cachupin.get_pasear():
                print(cachupin.get_nombre(), " pasea")
            else:
                print(cachupin.get_nombre(), " no pasea")
            cachupin.set_hora_toma_agua(1)
            cachupin.tomar_agua()
            print(cachupin.get_hora_toma_agua())
            cachupin.para()
            cachupin.set_hora_toma_agua(1)
            cachupin.tomar_agua()
            print(cachupin.get_hora_toma_agua())
            break
            
        break

if __name__ == "__main__":
    main()
