from secuenciador import Secuenciador
from secuenciaADN import SecuenciaADN

def main():
    sec = Secuenciador()
    sec.set_secuencia()
    print(sec.get_informacion())
    s1 = SecuenciaADN(sec.get_longitud(),sec.get_informacion())
    s1.set_cadena_inversa()
    s2 = SecuenciaADN(s1.get_longitud(),s1.get_reverso())
    s1.peso_molecular()
    s1.encontrar_patron("ACG")
if __name__ == "__main__":
    main()