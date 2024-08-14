#inicio del diccionario

"""se crea el diccionario y se agregan las palabras al diccionario ys e hace la lista,
   se crea la variable para acceder al diccionario, se crea un ciclo while que nos 
   permita seguir en el buscador y no se nos reinicie el programa, se usa la funcion 
   lower que nos permitre cambiar toda las palabrsas ingresadas a minusculas y asi no 
   importe si se ingresa en mmayuscula o minuscula, se llama ala variable del diccionario 
   y entra en funcion el lower y se imprime en pantalla el significado, se crea la variable 
   que permita conocer quien fue el creador y la funcion del diccionario, se crea el ciclo 
   while npara poder acceder al menu de cada u na de las variables y se imprime en pantalla 
   el menu, se crea la funcion que permita reiniciar el ciclo while y verifique si fue 
   ejecutado o no"""

diccionario = { #se crea el diccionario y se agregan las palabras al diccionario ys e hace la lista
    "computadora": "una máquina electrónica que procesa información y realiza tareas",
    "internet": "una red global de computadoras que se comunican entre sí",
    "programar": "crear instrucciones para que una computadora realice una tarea específica",
    "algoritmo": "un conjunto de instrucciones para resolver un problema o realizar una tarea",
    "base de datos": "un conjunto de datos organizados y almacenados de manera sistemática",
    "software": "programas y aplicaciones que se ejecutan en una computadora",
    "hardware": "componentes físicos de una computadora, como la CPU, memoria y dispositivos de entrada/salida",
    "red": "un conjunto de computadoras y dispositivos conectados entre sí para compartir recursos y comunicarse",
    "navegador": "un programa que permite acceder y navegar por la internet",
    "aplicación": "un programa que se utiliza para realizar una tarea específica, como editar texto o imágenes",
    "algoritmo": "secuencia de pasos para resolver un problema",
    "archivo": "conjunto de datos almacenados en un dispositivo",
    "binario": "sistema numérico de dos dígitos: 0 y 1",
    "bluetooth": "Ttecnología de comunicación inalámbrica de corto alcance",
    "cache": "almacenamiento temporal de datos para acceso rápido",
    "backup": "copia de seguridad de archivos o datos",
    "código Fuente": "instrucciones escritas en un lenguaje de programación",
    "compilador": "programa que traduce el código fuente a código máquina",
    "criptografía": "técnica de protección de información mediante el cifrado de datos",
    "ciberseguridad": "protección de sistemas y redes frente a ataques y accesos no autorizados",
    "driver": "programa que permite la comunicación entre el sistema operativo y un dispositivo hardware",
    "encriptación": "proceso de codificar datos para que solo sean legibles por quienes tienen acceso autorizado",
    "debugging": "proceso de encontrar y corregir errores en un programa",
    "cookie": "pequeño archivo de datos almacenado por un sitio web en el navegador del usuario",
    "bug": "error o fallo en un programa informático",
    "firmware": "software embebido en hardware que controla su funcionamiento",
    "firewall": "sistema de seguridad que controla el tráfico de red",
    "fuente de Poder": "componente de hardware que suministra energía eléctrica a una computadora",
    "gigabyte": "unidad de almacenamiento equivalente a 1024 megabytes",
    "hacker": "persona que manipula sistemas informáticos, a veces con intenciones maliciosas",
    "hardware": "componentes físicos de un sistema informático",
    "hosting": "servicio que almacena y sirve sitios web",
    "HTML": "lenguaje de programación utilizado para estructurar páginas web",
    "HTTP": "protocolo que permite la transferencia de información en la web",
    "IP": "dirección única asignada a cada dispositivo conectado a una red",
    "java": "lenguaje de programación ampliamente utilizado",
    "kernel": "núcleo del sistema operativo que gestiona recursos y la comunicación entre hardware y software",
    "LAN": "Red de computadoras dentro de un área limitada",
    "latencia": "Tiempo de retraso en la transmisión de datos",
    "licencia de Software": "Acuerdo legal que define cómo se puede utilizar un software",
    "malware": "Software malicioso diseñado para causar daño o acceso no autorizado a sistemas informáticos",
    "memoria RAM": "Memoria de acceso rápido utilizada por una computadora para almacenar temporalmente datos",
    "microprocesador": "Chip que ejecuta instrucciones en un sistema informático",
    "modem": "Dispositivo que convierte señales digitales en analógicas para la transmisión de datos a través de líneas telefónicas",
    "navegador": "Software que permite acceder a sitios web",
    "nodo": "Punto de conexión en una red",
    "código abierto": "Software cuyo código fuente está disponible para ser modificado y distribuido",
    "Operador Booleano": "Símbolos que representan relaciones lógicas en operaciones de búsqueda o programación (AND, OR, NOT)",
    "sistema Operativo": "Software que gestiona el hardware y software en un sistema informático",
    "paquete": "Unidad de datos transmitida a través de una red",
    "parche de Seguridad": "Actualización de software que corrige vulnerabilidades de seguridad",
    "contraseña": "Conjunto de caracteres que protege el acceso a sistemas o datos",
    "píxel": "Unidad mínima de una imagen digital",
    "placa Madre": "Tarjeta principal de un sistema informático que conecta todos los componentes",
    "complemento": "Extensión de software que añade funcionalidades a un programa",
    "procesador Gráfico": "Unidad encargada de procesar gráficos y vídeos en un sistema informático",
    "programador": "Persona que escribe código en lenguajes de programación",
    "protocolo": "Conjunto de reglas que permiten la comunicación entre dispositivos en una red",
    "proxy": "Servidor intermediario que facilita la conexión entre un usuario y un servidor",
    "RAID": "Configuración de múltiples discos duros que mejora el rendimiento o la seguridad",
    "Resolución": "Cantidad de píxeles que componen una imagen",
    "memoria de Solo Lectura": "Memoria que contiene datos permanentes en un sistema informático",
    "router": "Dispositivo que dirige el tráfico de datos entre diferentes redes",
    "script": "Conjunto de instrucciones ejecutadas por un programa o sistema operativo",
    "servidor": "Computadora que proporciona servicios o datos a otros dispositivos en una red",
    "software": "Programas y sistemas operativos que controlan el hardware",
    "spyware": "Software que recopila información sobre un usuario sin su conocimiento",
    "lenguaje de Consulta Estructurada": "Lenguaje utilizado para gestionar bases de datos",
    "unidad de Estado Sólido": "Dispositivo de almacenamiento más rápido que los discos duros tradicionales",
    "switch": "Dispositivo que conecta múltiples dispositivos en una red",
    "TCP/IP": "Protocolo de control de transmisión utilizado para el intercambio de datos en Internet",
    "teclado virtual": "Software que simula un teclado en pantalla",
    "terminal": "Interfaz de texto para interactuar con un sistema operativo",
    "troyano": "Tipo de malware que se disfraza como un software legítimo",
    "protocolo de datagramas de usuario": "Protocolo de red que permite la transmisión de datos sin confirmación de recepción",
    "interfaz de Usuario": "Elementos gráficos a través de los cuales un usuario interactúa con un programa",

}

def mostrar_diccionario():#se crea la variable para acceder al diccionario
    print("Diccionario:")
    for palabra, traduccion in diccionario.items():
        print(f"{palabra}: {traduccion}")

def buscar_palabra():#se crea un ciclo while que nos permita seguir en el buscador y no se nos reinicie el programa
    while True:
        palabra = input("Ingrese una palabra (o 'volver' para regresar al menú): ").lower()#se usa la funcion lower que nos permitre cambiar toda las palabrsas ingresadas a minusculas y asi no importe si se ingresa en mmayuscula o minuscula
        if palabra == "volver":
            break
        elif palabra in diccionario:
            print(f"La traducción de '{palabra}' es: {diccionario[palabra]}") #se llama ala variable del diccionario y entra en funcion el lower y se imprime en pantalla el significado
        else:
            print(f"Lo siento, no encontré la palabra '{palabra}' en el diccionario.")

def acerca_de():#se crea la variable que permita conocer quien fue el creador y la funcion del diccionario
    print("Acerca de:")
    print("Diccionario creado por Fernanda Torres")
    print("en este diccionario se basa en palabras sobre la informatica la cual nos da el significado de las palabras mas usadas y comunes en la informatica")

def main():
    while True:#se crea el ciclo while npara poder acceder al menu de cada u na de las variables y se imprime en pantalla el menu
        print("Menú:")
        print("1. Acceder al diccionario")
        print("2. Buscar palabra")
        print("3. Acerca de")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_diccionario()
        elif opcion == "2":
            buscar_palabra()
        elif opcion == "3":
            acerca_de()
        elif opcion == "4":
            print("Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":#se crea la funcion que permita reiniciar el ciclo while y verifique si fue ejecutado o no
    main()