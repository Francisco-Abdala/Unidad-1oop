from protein import Proteina
from proteina_estructural import ProteinaEstructural
from proteina_enzimatica import ProteinaEnzimatica
from proteina_mutante import ProteinaMutante
from secuenciaProteica import SecuenciaProteica
from analizador_proteico import AnalizadorProteico
def main():
    proteina = Proteina()
    proteina.set_nombre("Proteina 1")
    proteina.set_descripcion("Es una proteina bonita")
    proteina.set_secuencia()
    print(proteina.get_nombre())
    print(proteina.get_secuencia())
    
    estructural = ProteinaEstructural()
    estructural.set_nombre("Proteina 2")
    estructural.set_descripcion("Es una proteina estructural")
    estructural.set_secuencia()
    estructural.set_tipo()
    print(estructural.get_tipo())
    print(estructural.get_secuencia())
    print(estructural.get_nombre())
    enzimatica = ProteinaEnzimatica()
    enzimatica.set_nombre("Proteina 3")
    enzimatica.set_descripcion("Es una proteina enzimatica")
    enzimatica.set_secuencia()
    enzimatica.set_substrato("Glucosa")
    print(enzimatica.get_substrato())
    print(enzimatica.get_nombre())
    print(enzimatica.get_secuencia())
    mutante = ProteinaMutante()
    mutante.set_nombre("Proteina 4")
    mutante.set_descripcion("Es una proteina mutante")
    mutante.set_secuencia()
    mutante.set_mutacion()
    mutante.get_mutacion()
    mutante.get_nombre()
    secuencia= SecuenciaProteica()
    secuencia.set_lista(proteina)
    secuencia.set_lista(estructural)
    secuencia.set_lista(enzimatica)
    secuencia.get_lista()
    secuencia.mostrar_secuencia(0)
    analizador = AnalizadorProteico()
    analizador.set_lista(proteina)
    analizador.set_lista(estructural)
    analizador.set_lista(enzimatica)
    analizador.set_lista(mutante)
    analizador.suma(0)

    """"
    parametro.isnumeric():
        parametro_int = int(parametro)
    if parametro_int: < len(lista):
        llamo funcion
    """
    """"
    """
if __name__ == "__main__":
    main()