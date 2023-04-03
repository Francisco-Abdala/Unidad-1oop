from vacuna import Vacuna
def main():
    #Lista en la que se almacenan los objetos tipo Vacuna
    #Solo es donde se guardan, sigo trabajando con los objetos
    vacunas = []

    #Ciclo que me permitirá crear "n" objetos
    while True:
        objeto1 = Vacuna()
        vacuna1= input("ingrese el nombre de su vacuna: ")
        objeto1.set_nombre_vacuna(vacuna1)
        lab1= input(f"Ingrese el nombre del laboratorio a que pertenece {vacuna1}: ")
        objeto1.set_lab(lab1)

        #Ciclo que me permitirá crear "n" efectos secundarios
        while True:
            x = input(f"Ingrese los efectos secundarios para {vacuna1}, debe ingresar al menos dos (2).Ingrese 0 para terminar: ")
            if x == "0" and len(objeto1.get_efectos()) > 1:
                break
            objeto1.set_agrega_efecto_secundario(x)
        
        #Guarda el objeto en la lista
        vacunas.append(objeto1)

        #Pregunta para saber si quiere tener otro objeto tipo vacuna
        continuar = input("¿Desea continuar agregando vacunas? (1) para sí, (0) para no: ")
        if continuar.isnumeric():
            continuar_int = int(continuar)
        if continuar_int == 1:
            continue
        if continuar_int == 0 and len(vacunas) >= 3:
            break
        if continuar_int == 0 and len(vacunas) < 3:
            print("La cantidad minima de vacunas es tres (3).Volverá al menu de ingreso de vacunas hasta que se cumpla esta condición")
            continue
        else:
            print("Dato/tipo de dato equivocado, se cierra el programa")
            break
    
    #Le muestra al usuario la cantidad de vacunas que tiene almacenada
    print("Las vacunas almacenadas son las siguientes:")
    for i in range(len(vacunas)):  
        print(vacunas[i].get_nombre())
        print("\n")

    #Pregunta para ver los efectos secundarios de una vacuna en especifico
    ayuda = input("Al ver la lista de vacunas,¿de cuál quiere conocer los efectos secundarios?: ")

    #Encuentra la vacuna y le entrega los efectos secundarios
    for i in range (len(vacunas)):
        if vacunas[i].get_nombre().lower() == ayuda.lower():
            print(vacunas[i].mostrar_efectos())
    
        

if __name__ == "__main__":
    main()


