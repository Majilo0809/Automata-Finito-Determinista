import sys

def simular(palabra):

    estado = 1  # estado inicial (q1)

    for caracter in palabra:

        # q1
        if estado == 1:
            if caracter == '0':
                estado = 2   # va a q2 (aceptación)
            elif caracter == '1':
                estado = 3   # va a q3 (rechazo)
            else:
                return False

        # q2 (estado de aceptación)
        elif estado == 2:
            if caracter == '0':
                estado = 2
            elif caracter == '1':
                estado = 2
            else:
                return False

        # q3 (estado de rechazo)
        elif estado == 3:
            if caracter == '0':
                estado = 3
            elif caracter == '1':
                estado = 3
            else:
                return False

    # Estado de aceptación es q2 (estado 2)
    if estado == 2:
        return True
    else:
        return False


# Main
if len(sys.argv) != 2:
    print("Uso: python AFD.py entrada.txt")
    sys.exit(1)

archivo = sys.argv[1]

with open(archivo, "r") as f:
    for linea in f:

        cadena = linea.strip()

        if simular(cadena):
            print("ACEPTA")
        else:
            print("NO ACEPTA")
