from PIL import Image
from os import system
import random
import threading

imagen1 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Foto_original.png"                                     #FOTO ORIGINAL
imagen2 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Angel_abajo.png"
imagen3 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Aprobado.png"
imagen4 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Araña_gigante.png"
imagen5 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Araña_tortuga.png"
imagen6 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Bola_nieve.png"
imagen7 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Bolas_arbol.png"
imagen8 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Calcetines.png"
imagen9 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Calendario.png"
imagen10 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Chinchetas.png"
imagen11 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Cuadro.png"
imagen12 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Decoracion_tablon.png"
imagen13 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Duende.png"
imagen14 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Estrella_arbol.png"
imagen15 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Horario_navidad.png"
imagen16 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Luces_colores.png"
imagen17 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Muñeco_galleta.png"
imagen18 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Niña.png"
imagen19 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Niña_volteada.png"
imagen20 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Pajaro.png"
imagen21 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Papel_derecho.png"
imagen22 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Regalo_vidrio.png"
imagen23 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Regalos_muchos.png"
imagen24 = "C:\\Users\\sergi\\OneDrive\\Escritorio\\Imagenes\\Simbolo_horario.png"

imagenes = [imagen1] * 16 + [imagen2, imagen3, imagen4, imagen5, imagen6, imagen7, imagen8, imagen9, imagen10, imagen11, imagen12, imagen13, imagen14, imagen15, imagen16, imagen17, imagen18, imagen19, imagen20, imagen21, imagen22, imagen23, imagen24]
print("\nHa aparecido un bucle temporal en navidad, debes cerrarlo para evitar que se lleven los regalos\n")

input("Presiona \033[1m\033[37mENTER\033[0m para \033[7m\033[35mabrir el bucle\033[0m")
system("cls")
print("""Al parecer, \033[32mesta imagen representa la realidad\033[0m, sin embargo, \033[32mexisten imagenes muy parecidas con diferentes\033[0m \033[31manomalías\033[0m.
Debes averiguar si las siguientes imagenes son iguales que esta, o por el contrario están afectadas por las anomalías.
Cuando \033[32mdescifres 8 seguidas\033[0m, el bucle se cerrará y habrás salvado la navidad, sin embargo, si fallas volverás al inicio del bucle.
Date prisa, solo \033[32mdispones de 15 segundos\033[0m para comprobar cada imagen""")
imagen = Image.open(imagen1)
nuevo_tamano = (1920, 1080)
imagen_redimensionada = imagen.resize(nuevo_tamano)
imagen_redimensionada.show()

contador = 0


def codigo_juego():

    
    global imagen_cambiada, contador, imagen1
    input("\nPresiona \033[1m\033[37mENTER\033[0m para \033[7m\033[35mentrar en el bucle\033[0m")
    system("cls")
    imagen_seleccionada = random.choice(imagenes)

    imagen_cambiada = Image.open(imagen_seleccionada)
    nuevo_tamaño = (1920, 1080)
    imagen_redimensionada = imagen_cambiada.resize(nuevo_tamaño)
    imagen_redimensionada.show()
    print("¿Has encontrado anomalías en la imagen?\n")
    print("1. Hay \033[31manomalías\033[0m\n2. No hay anomalías")

    temporizador = threading.Timer(15, tiempo_agotado)                                                #TEMPORIZADOR
    temporizador.start()
    print("\nTienes \033[32m15 segundos\033[0m para escapar o el bucle se cerrará para siempre\n")


    try:
        accion = int(input("Acción: "))
    except ValueError:
        accion = int(input("Acción: "))



    temporizador.cancel()
    system("cls")

    if accion == 1 and imagen_seleccionada != imagen1:
        contador = contador + 1
        print (f"Has pasado al nivel {contador}")
    elif accion == 1 and imagen_seleccionada == imagen1:
        contador = 0
        print (f"Has fallado, el bucle volvió al nivel {contador}")
    elif accion == 2 and imagen_seleccionada != imagen1:
        contador = 0
        print (f"Has fallado, el bucle volvió al nivel {contador}")
    elif accion == 2 and imagen_seleccionada == imagen1:
        contador = contador + 1
        print (f"Has descifrado la imagen, has subido al nivel {contador} del bucle")
    else:
        pass
        

def tiempo_agotado():
    global contador
    contador = 0
    print("\n\nTiempo agotado, el bucle se ha cerrado...")

while True:
    if contador > 8:                                                                                       #FINALIZAR JUEGO
         break

    codigo_juego()


print("Saliste del bucle, has salvado la navidad")