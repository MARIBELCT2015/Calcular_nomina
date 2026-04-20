# ==========================================
# SIMULADOR MATRÍCULA - UNAD
#UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA - UNAD
#Curso: Estructura de datos - Programación en Python
#Aplicación: Simulador de Matrícula
#Descripción:
#Sistema que calcula el valor de matrícula según:
#- Cantidad de créditos
#- Estrato socioeconómico
#- Certificado electoral

#Se implementa:
#Programación Orientada a Objetos
#Estructuras de Datos Dinámicas
#Lista Enlazada
#Diccionario (tabla hash)
#Inserción, eliminación y recorrido
#Gestión de memoria en tiempo de ejecución
# ==========================================


# --------- PRIMERA INTERFAZ (LOGIN) ---------
def pantalla_inicio():  # Define la función que muestra la pantalla inicial y valida el acceso

    print("==============================================")  # Imprime línea decorativa superior
    print("Nombre del estudiante: Maribel Cifuentes Torres")  # Muestra el nombre completo del estudiante
    print("Aplicación: Simulador Matricula")  # Muestra el nombre de la aplicación
    print("Curso: Estructura de Datos")  # Muestra el nombre del curso
    print("==============================================")  # Imprime línea decorativa inferior

    password = input("Ingrese la contraseña de acceso (2046): ")  
    # Solicita al usuario la contraseña de acceso y la almacena en la variable password

    if password == "2046":  
        # Verifica si la contraseña ingresada coincide con la contraseña genérica establecida

        print("\nAcceso concedido.\n")  
        # Muestra mensaje indicando que la autenticación fue correcta

        return True  
        # Retorna True para indicar que el acceso fue autorizado

    else:  
        # Si la contraseña no coincide

        print("Contraseña incorrecta. Acceso denegado.")  
        # Muestra mensaje de error indicando que el acceso fue rechazado

        return False  
        # Retorna False para indicar que no se permite el acceso al sistema


# --------- SEGUNDA INTERFAZ (MENÚ) ---------
def menu_principal():  # Define la función que controla el menú principal del sistema

    lista = ListaEnlazada()  # Crea un objeto de tipo ListaEnlazada para almacenar los estudiantes dinámicamente

    while True:  # Inicia un ciclo infinito para mantener el menú activo hasta que el usuario decida salir

        print("\n========== MENÚ PRINCIPAL ==========")  # Muestra el título del menú
        print("1. Insertar estudiante")  # Opción 1: Agregar estudiante
        print("2. Mostrar estudiantes")  # Opción 2: Mostrar todos los estudiantes
        print("3. Eliminar estudiante")  # Opción 3: Eliminar un estudiante por ID
        print("4. Salir")  # Opción 4: Salir del programa

        opcion = input("Seleccione una opción: ")  # Captura la opción ingresada por el usuario (tipo texto)

        if opcion == "1":  # Verifica si el usuario eligió insertar estudiante

            try:  # Intenta ejecutar el bloque para validar datos numéricos
                identificacion = int(input("ID: "))  # Solicita el ID y lo convierte a entero
                creditos = int(input("Créditos (1-21): "))  # Solicita créditos y los convierte a entero
                estrato = int(input("Estrato (1-6): "))  # Solicita estrato y lo convierte a entero
            except ValueError:  # Captura error si el usuario ingresa texto en vez de número
                print("Error: Ingrese valores numéricos.")  # Muestra mensaje de error
                continue  # Regresa al inicio del menú

            nombre = input("Nombre: ")  # Solicita el nombre del estudiante
            genero = input("Género: ")  # Solicita el género del estudiante
            certificado = input("Certificado electoral (si/no): ")  # Solicita si tiene certificado electoral

            estudiante = Estudiante(  # Crea un objeto de la clase Estudiante
                identificacion, nombre, genero,  # Envía ID, nombre y género al constructor
                creditos, estrato, certificado  # Envía créditos, estrato y certificado al constructor
            )

            lista.insertar(estudiante)  # Inserta el objeto estudiante dentro de la lista enlazada
            print("Estudiante agregado correctamente.")  # Confirma que fue agregado

        elif opcion == "2":  # Verifica si el usuario eligió mostrar estudiantes
            lista.recorrer()  # Llama al método recorrer para mostrar todos los nodos de la lista

        elif opcion == "3":  # Verifica si el usuario eligió eliminar estudiante

            try:  # Intenta convertir el ID ingresado a entero
                id_eliminar = int(input("Ingrese ID a eliminar: "))  # Solicita el ID a eliminar
            except ValueError:  # Si ocurre error por valor no numérico
                print("ID inválido.")  # Muestra mensaje de error
                continue  # Regresa al inicio del menú

            lista.eliminar(id_eliminar)  # Llama al método eliminar pasando el ID como argumento

        elif opcion == "4":  # Verifica si el usuario eligió salir
            print("Saliendo del sistema...")  # Muestra mensaje de salida
            break  # Rompe el ciclo while y termina el menú

        else:  # Si el usuario escribe una opción diferente
            print("Opción inválida.")  # Muestra mensaje de opción incorrecta

# --------- TABLA DINÁMICA DE CRÉDITOS ---------
TABLA_CREDITOS = {
    1: 159000,
    2: 318000,
    3: 477000,
    4: 636000,
    5: 795000,
    6: 954000,
    7: 1113000,
    8: 1272000,
    9: 1431000,
    10: 1590000,
    11: 1749000,
    12: 1908000,
    13: 2067000,
    14: 2226000,
    15: 2385000,
    16: 2544000,
    17: 2703000,
    18: 2862000,  
    19: 3021000,
    20: 3180000,
    21: 3339000
}

# --------- CLASE ESTUDIANTE ---------
class Estudiante: #Definir la clase estudiante, los : puntos indican un bloque de código

    def __init__(self, identificacion, nombre, genero, creditos, estrato, certificado): # Definir la función, (__init__) es un método constructor, sirve para iniciar los atributos
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.creditos = creditos
        self.estrato = estrato
        self.certificado = certificado.lower() #Convierte el texto a minúsculas.Para evitar errores cuando el usuario escriba diferente.
        #self representa: El objeto que se está creando en ese momento. Es obligatorio en métodos de clase. Sin self, Python no sabría a qué objeto pertenecen las variables.

    def calcular_matricula(self): #def → Define una función. calcular_matricula → Nombre del método. 

        if self.creditos not in TABLA_CREDITOS: #(self) → Hace referencia al objeto actual. # TABLA_CREDITOS: es un diccionario. #Validar que el estudiante ingrese 25 créditos.
            return None #Devuelve un valor. #Significa "no hay resultado válido".Porque si los créditos no existen,nNo se puede calcular matrícula. Entonces el método termina inmediatamente.
        valor_base = TABLA_CREDITOS[self.creditos] #TABLA_CREDITOS es un diccionario.  self.creditos es la clave. Se obtiene el valor correspondiente.

        # Descuento por estrato
        if self.estrato in [1, 2]: #self.estrato es un atributo del objeto. Está preguntando: ¿El estrato del estudiante es 1 o 2?
            descuento_estrato = valor_base * 0.15 #Si el estrato es 1 o 2: Se aplica 15% o el 0.15 es la representación decimal del 15%
        elif self.estrato in [3, 4]:
            descuento_estrato = valor_base * 0.10
        elif self.estrato in [5, 6]:
            descuento_estrato = valor_base * 0.05
        else:
            descuento_estrato = 0  #Si el estrato no es válido: No aplica descuento, se evita que la variable quede sin valor

        valor_con_estrato = valor_base - descuento_estrato # Aquí se hace la operación matemática final

        # Descuento certificado electoral
        if self.certificado == "si": #Está preguntando: ¿El estudiante presentó certificado electoral?
            descuento_certificado = valor_con_estrato * 0.10  
        else:
            descuento_certificado = 0

        valor_final = valor_con_estrato - descuento_certificado #Este es el monto real de matrícula.

        return valor_base, descuento_estrato + descuento_certificado, valor_final #Aquí estás devolviendo 3 valores al mismo tiempo.#Python permite retornar múltiples valores como tupla.#Lo que realmente se retorna es:


        # --------- NODO ---------
class Nodo:  
    # Define la clase Nodo, que representa cada elemento de la lista enlazada

    def __init__(self, estudiante):  
        # Constructor de la clase Nodo
        # Recibe como parámetro un objeto estudiante que será almacenado en el nodo

        self.estudiante = estudiante  
        # Guarda el objeto estudiante dentro del nodo
        # Este es el dato que contiene el nodo

        self.siguiente = None  
        # Inicializa la referencia al siguiente nodo como None
        # Esto significa que inicialmente el nodo no apunta a nadie



# --------- LISTA ENLAZADA ---------
#es la base de la estructura dinámica (lista enlazada).
class ListaEnlazada:  # Se define una nueva clase llamada Nodo.

    def __init__(self): 
        self.cabeza = None

    def insertar(self, estudiante): #Se guarda el dato dentro del nodo.

        nuevo_nodo = Nodo(estudiante) #Crea un nuevo nodo, conectar ese nodo a la lista y luego se guarda la referencia estudiante

        if self.cabeza is None: #primer nodo de la lista. La cabeza es: El punto de inicio de la lista enlazada. Si la lista NO está vacía, debemos insertar al final.
            self.cabeza = nuevo_nodo #La condición significa que ¿La lista está vacía? Si cabeza es None, significa que no hay ningún nodo todavía.
        else:
            actual = self.cabeza #Se crea una variable auxiliar llamada actual.
            while actual.siguiente: #Mientras exista un siguiente nodo 
                actual = actual.siguiente #Aquí se esta avanzando nodo por nodo.
            actual.siguiente = nuevo_nodo #El último nodo ahora apunta al nuevo nodo.
#estructura dinámica:  Inserción, Eliminación, Recorrido
    def recorrer(self): #Pasar por cada nodo de la lista uno por uno desde la cabeza hasta el final.

        actual = self.cabeza #Crear una variable auxiliar llamada actual.

        if actual is None:
            print("\nNo hay estudiantes registrados.")
            return
#Entonces: Si la lista tiene nodos → actual apunta al primer nodo #Si la lista está vacía → self.cabeza = None → entonces actual = None
        while actual: #recorrido + acceso a objeto + llamada a método, o sea programación orientada a objetos aplicada sobre una estructura dinámica.
            est = actual.estudiante #En esta pequeña parte del código estás combinando: Recorrido de estructura dinámica, Acceso a datos encapsulados # Llamada a método de clase # Cálculo interno usando atributos privados
            resultado = est.calcular_matricula()

            print("\n----------------------------------")  
            # Imprime una línea separadora con salto de línea para organizar la salida en pantalla

            print("ID:", est.identificacion)  
            # Muestra el ID del estudiante accediendo al atributo identificacion del objeto est

            print("Nombre:", est.nombre)  
            # Muestra el nombre del estudiante accediendo al atributo nombre del objeto est


            if resultado:  
                # Verifica si el método calcular_matricula devolvió un resultado válido (no es None)

                base, descuento, total = resultado  
                # Desempaqueta la tupla retornada en tres variables:
                # base → valor base de la matrícula
                # descuento → suma total de descuentos aplicados
                # total → valor final a pagar

                print("Valor Base: $", base)  
                # Muestra el valor base de la matrícula

                print("Descuento Total: $", int(descuento))  
                # Muestra el descuento total convertido a entero para evitar decimales

                print("Valor Final a Pagar: $", int(total))  
                # Muestra el valor final convertido a entero para una mejor presentación

            else:  
                # Si resultado es None (por ejemplo créditos fuera de rango)

                print("Créditos inválidos.")  
                # Muestra mensaje indicando que los créditos ingresados no son válidos


            actual = actual.siguiente  
            # Avanza al siguiente nodo de la lista enlazada para continuar el recorrido



    def eliminar(self, identificacion):  
        # Define el método eliminar que recibe como parámetro el ID del estudiante a eliminar


        actual = self.cabeza  
        # Inicializa la variable actual apuntando al primer nodo de la lista

        anterior = None  
        # Inicializa la variable anterior en None (se usará para mantener referencia al nodo previo)


        while actual and actual.estudiante.identificacion != identificacion:  
            # Recorre la lista mientras:
            # 1. Exista un nodo actual
            # 2. El ID del estudiante no coincida con el ID a eliminar

            anterior = actual  
            # Guarda el nodo actual como nodo anterior antes de avanzar

            actual = actual.siguiente  
            # Avanza al siguiente nodo de la lista


        if actual is None:  
            # Si actual es None significa que no se encontró el estudiante

            print("Estudiante no encontrado.")  
            # Muestra mensaje indicando que el ID no existe en la lista

            return  
            # Sale del método sin hacer modificaciones


        if anterior is None:  
            # Si anterior es None significa que el nodo a eliminar es el primero (la cabeza)

            self.cabeza = actual.siguiente  
            # Actualiza la cabeza para que apunte al siguiente nodo, eliminando el primero

        else:  
            # Si no es el primer nodo

            anterior.siguiente = actual.siguiente  
            # El nodo anterior ahora apunta al siguiente del nodo actual,
            # desconectando así el nodo eliminado de la lista


        print("Estudiante eliminado correctamente.")  
        # Confirma que la eliminación se realizó con éxito

# --------- PROGRAMA PRINCIPAL ---------

def main():  # Define la función principal del programa

    acceso = pantalla_inicio()  # Llama a la función pantalla_inicio para validar contraseña

    if acceso:  # Si la contraseña es correcta (True)
        menu_principal()  # Ejecuta el menú principal


if __name__ == "__main__":  # Verifica que el archivo se esté ejecutando directamente
    main()  # Llama a la función principal para iniciar el programa