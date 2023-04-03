from planeta import Planeta
from sistema import Sistema

def main():
    sistema = Sistema()
    contador = 0
    #Se le da la oportunidad a Urano de ser un planeta
    while contador < 8:
        planeta = Planeta()
        nombre = input("Ingrese el nombre del planeta: ")
        planeta.set_nombre(nombre)
        #Seguidilla de while para validar que cada dato sea un entero
        while True:
            masa = input("Ingrese la masa del planeta: ")
            if masa.isnumeric():
                masa_int = int(masa)
                planeta.set_masa(masa_int)
                break
            else:
                print("Ingrese un dato númerico.")
                continue
        while True:
            densidad = input("Ingrese la densidad del planeta: ")
            if densidad.isnumeric():
                densidad_int = int(densidad)
                planeta.set_densidad(densidad_int)
                break
            else:
                print("Ingrese un dato númerico.")
                continue
        while True:
            diametro = input("Ingrese el diametro del planeta: ")
            if diametro.isnumeric():
                diametro_int = int(diametro)
                planeta.set_diametro(diametro_int)
                break
            else:
                print("Ingrese un dato númerico.")
                continue
        #Se separa el identificador en dos partes para que tenga digito/s verificador/es
        while True:
            identificador_str = input("Ingrese el identificador del planeta (puede ser letras o números): ")
            while True:
                identificador_int = input("Ingrese el digito verificador (debe ser si o si un/unos número/s): ")
                if identificador_int.isnumeric():
                    identificador = identificador_str + "-" + identificador_int
                    planeta.set_identificador(identificador)
                    break
                else:
                    print("Debe ser una combinación de números y letras.")
                    continue
            break
        #Se ingresa la clase planeta a la clase sistema
        sistema.set_sistema(planeta)
        contador += 1
        if contador <= 7:
            print("Ingrese otro planeta")
    print("Estos son los planetas registrados: ")
    sistema.mostrar_sistema()
    atributos = input("ingrese el planeta del que desea saber los atributos: ")
    sistema.mostrar_atributos(atributos)
                
if __name__ == "__main__":
    main()