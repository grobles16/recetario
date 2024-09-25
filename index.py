from pathlib import Path
from os import system
import os
from shutil import rmtree

ruta_base = "Recetas"
opcion_menu = 0
opcion_categoria = 0
opcion_receta = 0
nombre_categoria = ''
nombre_receta = ''
bandera = False
bandera_categoria = False
bandera_receta = False


def limpiar_consola():
    system('cls')
    return

def validar_respuesta(numero):
    numeros = '1234567890'

    if numero in numeros:
        return True
    else:
        print("- - Ingrese una opcion valida para continuar - -")
        return False
    
def validar_nombre_receta(categoria, receta):

    url = Path(ruta_base ,categoria, receta + '.txt') 
    receta = os.path.isfile(url)    

    if receta == True:
        print('\n-------------------------------------')
        print('| Ya existe un receta con ese nombre |')
        print('-------------------------------------\n')
        return True
    else:
        return False

def validar_nombre_categoria(categoria):

    url = Path(ruta_base ,categoria) 
    categoria = os.path.isdir(url)    

    if categoria == True:
        print('\n-------------------------------------')
        print('| Ya existe una categoria con ese nombre |')
        print('-------------------------------------\n')
        return True
    else:
        return False

def menu():

    print("\n* * Bienvenido a mi recetario * *")
    print (
        "[1] - Leer receta\n"
        "[2] - Crear receta\n"
        "[3] - Crear Categoría\n"
        "[4] - Eliminar Receta\n"
        "[5] - Eliminar Categoría\n"
        "[6] - Finalizar programa"
    )
    return

def obtener_recetas(categoria):
    listado_recetas = []

    for txt in Path(ruta_base, categoria).glob("**/*.txt"):
        listado_recetas.append(txt.name)
    
    return sorted(listado_recetas)


def obtener_categorias():
    listado_categorias = []

    for txt in Path(ruta_base).glob("**/*"):
        if txt.parent.name not in listado_categorias:
            listado_categorias.append(txt.name)

    return listado_categorias

def mostrar_listados(lista):
    index = 0
    print('\n')
    for l in lista:
        print(f"[{index}]: {l}")
        index += 1
    return

def abrir_receta(categoria, archivo):
    url = Path(ruta_base, categoria, archivo)
    archivo = open(url)
    limpiar_consola()
    print('*************************')
    print(archivo.read())
    print('*************************')
    archivo.close()
    return

def eliminar_receta(categoria, archivo):
    url = Path(ruta_base, categoria, archivo)
    if os.path.exists(url):
         os.remove(url)
         limpiar_consola()
         print(f"- - - - - La receta {url} ha sido eliminado - - - - -")

def eliminar_categoria(categoria):
    categoria = Path(ruta_base, categoria)

    if os.path.exists(categoria):
        rmtree(categoria)
        limpiar_consola()
        print(f"La carpeta {categoria} ha sido eliminada con todos sus elementos")
    else:
        print("La carpeta no existe")

def crear_receta(categoria, receta):
    
    archivo = open(Path(ruta_base, categoria, receta + '.txt'), 'x')
    archivo.close()
    limpiar_consola()
    print(f"- - - Se creo la receta ({receta}.txt)- - -")
    return

def crear_categoria(categoria):
    
    archivo = os.mkdir(Path(ruta_base, categoria))
    limpiar_consola()
    print(f"- - - - - Nueva categoria agregada - - - - -")
    return

limpiar_consola()
menu()
while bandera == False:
    opcion_menu = input("Ingerese una opcion del menú: ")
    if validar_respuesta(opcion_menu) == True:
        if opcion_menu == '1':
            categorias = obtener_categorias()
            mostrar_listados(categorias)

            while bandera_categoria == False:
                opcion_categoria = input("Seleccione una categoria: ")
                if validar_respuesta(opcion_categoria) == True:
                    if int(opcion_categoria) < len(categorias):
                        bandera_categoria = True
                    else:
                        print('- - - - Ingrese una opcion valida del menu de categorias - - - -')
                
            recetas = obtener_recetas(categorias[int(opcion_categoria)])
            mostrar_listados(recetas)

            while bandera_receta == False:
                opcion_receta = input("Seleccione una receta que desee leer: ")
                if validar_respuesta(opcion_receta) == True:
                    if int(opcion_receta) < len(recetas):
                        bandera_receta = True
                    else:
                        print('- - - - Ingrese una opcion valida del menu de recetas - - - -')

            abrir_receta(categorias[int(opcion_categoria)], recetas[int(opcion_receta)])
        
        elif opcion_menu == '2':
            categorias = obtener_categorias()
            mostrar_listados(categorias)

            while bandera_categoria == False:
                opcion_categoria = input("Seleccione la categoria que va asignar a su nueva receta: ")
                if validar_respuesta(opcion_categoria) == True:
                    if int(opcion_categoria) < len(categorias):
                        bandera_categoria = True
                    else:
                        print('- - - - Ingrese una opcion valida del menu de categorias - - - -')

            while bandera_receta == False:
                nombre_receta = input("Escriba el nombre de su nueva receta sin extension(.txt): ")

                if validar_nombre_receta(categorias[int(opcion_categoria)], nombre_receta) == False:
                    crear_receta(categorias[int(opcion_categoria)], nombre_receta)
                    bandera_receta = True

        elif opcion_menu == '3':
            while bandera_categoria == False:
                nombre_categoria = input("Escriba el nombre de su nueva categoria: ")
                if validar_nombre_categoria(nombre_categoria) == False:
                    crear_categoria(nombre_categoria)
                    bandera_categoria = True
        
        elif opcion_menu == '4':
            categorias = obtener_categorias()
            mostrar_listados(categorias)

            while bandera_categoria == False:
                opcion_categoria = input("Seleccione una categoria: ")
                if validar_respuesta(opcion_categoria) == True:
                    if int(opcion_categoria) < len(categorias):
                        bandera_categoria = True
                    else:
                        print('- - - - Ingrese una opcion valida del menu de categorias - - - -')
                
            recetas = obtener_recetas(categorias[int(opcion_categoria)])
            mostrar_listados(recetas)

            while bandera_receta == False:
                opcion_receta = input("Seleccione la receta que desea eliminar: ")
                if validar_respuesta(opcion_receta) == True:
                    if int(opcion_receta) < len(recetas):
                        bandera_receta = True
                    else:
                        print('- - - - Ingrese una opcion valida del menu de recetas - - - -')

            eliminar_receta(categorias[int(opcion_categoria)], recetas[int(opcion_receta)])

        elif opcion_menu == '5':
            categorias = obtener_categorias()
            mostrar_listados(categorias)

            while bandera_categoria == False:
                opcion_categoria = input("Seleccione una categoria para eliminar: ")
                if validar_respuesta(opcion_categoria) == True:
                    if int(opcion_categoria) < len(categorias):
                        bandera_categoria = True
                    else:
                        print('- - - - Ingrese una opcion valida del menu de categorias - - - -')

            eliminar_categoria(categorias[int(opcion_categoria)])

        elif opcion_menu == '6':
            bandera = True
            print("- - - - - Se finalizo el recetario - - - - -")
            
        elif opcion_menu not in '123456':
            print("* * * * Ingrese un valor del 1 al 6 * * * *")

    bandera_receta = False
    bandera_categoria = False
    menu()



