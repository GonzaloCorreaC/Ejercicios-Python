##ej1
#rut = input("Ingrese su rut (Sin punton ni guion): ")

#if len(rut) >= 8 and len(rut) <= 9 and rut.isdigit():
    #print("Rut valido")
#else:
    #print("Rut invalido")

##ej2
#correo = input("Ingrese un correo: ")
#correo = correo.strip().lower()

#if "@" in correo:
    #print(f"Correo ingresado: {correo}")
#else:
    #print("Correo invalido")

##ej3
#titulo = input("Ingrese el titulo de un libro: ")
#titulo = titulo.title()
#print(f"Formato valido: {titulo}")

##ej4
#frase = input("Ingrese una frase: ")
#frase = frase.lower()

#if "python" in frase:
    #print("Se encuentra la palabra Python en su frase")
#else:
    #print("No se encuentra la palabra python en su frase")

##ej5
#patente = input("Ingrese una patente chilena (4 letras y 2 numeros): ")

#if patente[-2:].isdigit():
    #print("Formato correcto")
#else:
    #print("Formato invalido")

##ej6
#comentario = input("Comentario de usuario: ")
#comentario = comentario.replace("malo","****")
#print(f"Comentario final: {comentario}")

##ej7
#url = input("Ingrese una URL: ")
#if url.startswith("https://"):
    #print(f"Dominio {url[8:]}")
#else:
    #print("URL invalida")

##ej8
#frase = input("Ingrese una frase: ")
#frase = frase.split()
#print(f"La frase tiene {len(frase)} palabras")

##ej9
#verificador = input("Ingrese un codigo de producto: ")

#if verificador.isupper():
    #print("Codigo valido")
#else:
    #print("Codigo invalido")

##ej10
#nombre = input("Ingrese un nombre: ")
#nombre = nombre.replace("  "," ")
#print(f"Nombre corregido: {nombre}")



print