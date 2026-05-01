#nombre = input("Ingrese un nombre: ")

#if len(nombre) > 5 and len(nombre) < 15 and nombre[0].isalpha() and nombre.isalnum():
    #print(f"Nombre ingresado {nombre} valido")
#elif len(nombre) <= 5 and len(nombre) <= 15:
    #print("El nombre debe tener mas de 5 y menos de 15 caracteres")
#else:
    #print("El usuario debe ser alfanumerico y empezar en una letra")

#contraseña = input("Ingrese la contraseña: ")

#if len(contraseña) >= 8 and not contraseña.isalpha() and not contraseña.isnumeric() and contraseña.find(" ") == -1:
    #print("Contraseña fuerte")
#elif len(contraseña) < 8:
    #print("Contraseña demasia corta")
#else:
    #print("La contraseña debe incluir letras y numeros y no tener espacios")

#nombre = input("Ingresa un nombre: ")

#if nombre.islower() or nombre.isupper():
    #nombre = nombre.title()
    #print(f"Nombre en formato correcto: {nombre}")
#elif nombre == "":
    #print("El nombre no puede estar vacio")
#else:
    #print(f"Nombre correcto: {nombre}")

#correo = input("Correo: ")

#if correo.count("@") == 1 and not correo.startswith("@") and (correo.endswith(".com") or correo.endswith(".org")):
    #print("Correo valido")
#elif correo.count("@") != 1:
    #print("El correo de contener exactamente un @")
#else:
    #print("El correp debe terminar en .com o .org")

#palabra = input("Ingrese una palabra: ")
#palabra_limpia = palabra.replace(" ", "").lower()

#if len(palabra_limpia) > 0 and palabra_limpia == palabra_limpia[::-1]:
    #print("Es un palidromo")
#elif len(palabra_limpia) == 0:
    #print("Error: entrada vacia")
#else:
    #print("No es un palidromo")

#archivo = input("Ingrese el nombre del archivo: ")
#archivo = archivo.lower()

#if archivo.endswith(".jpg") or archivo.endswith(".png") or archivo.endswith(".gif"):
    #print("El archivo es una imagen")
#elif archivo.endswith(".pdf") or archivo.endswith(".doc"):
    #print("El archivo es un documento")
#else:
    #print("El archivo es de formato desconocido")

#url = input("Ingrese una URL: ")

#if url.startswith("https://") or url.startswith("http://"):
    #sin_protocolo = url.split("://")[1]
    #if "/" in sin_protocolo:
        #dominio = sin_protocolo.split("/")[0]
    #else:
        #dominio = sin_protocolo
    #print(f"El dominio es: {dominio}")
#elif url == "":
    #print("URL vacia")
#else:
    #print("Error: La URL debe comenzar con http:// o https://")

#comentario = input("Ingresa un comentario: ")
#comentario = comentario.strip().lower()

#if comentario == "":
    #print("El cometario no debe estar vacio")
#elif "tonto" in comentario or "feo" in comentario:
    #comentario_limpio = comentario.replace("tonto", "****").replace("feo", "***")
    #print(f"Comentario censurado: {comentario_limpio}")
#else:
    #print(f"Comentario publicado: {comentario}")

#codigo = input("Ingresa el codigo del producto: ")
#codigo = codigo.strip().upper()

#if codigo.startswith("PROD-") and len(codigo) == 9 and codigo[5:].isdigit():
    #print("Codigo de producto valido")
#elif not codigo.startswith("PROD-"):
    #print("Error: El codigo de empezar en PROD-")
#else:
    #print("Error: La parte final debe contener exactamente 4 digitos numericos")

#nombre = input("Ingresa tu nombre: ")
#apellido = input("Ingresa tu apellido: ")

#if nombre.isalpha() and apellido.isalpha() and len(nombre) > 0 and len(apellido) > 0:
    #usuario = (nombre[0] + apellido).lower()
    #print(f"Su nombre de usuario es: {usuario}")
#elif nombre == "" or apellido == "":
    #print("Error: Debe igresar ambos datos")
#else:
    #print("Error: El nombre y apellido solo deben contener letras")

