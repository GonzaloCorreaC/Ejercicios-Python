##BLOQUE1##
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

##ej11
#texto = input("Ingrese el texto: ")
#texto = texto.lower

#if texto.endswith(".pdf") and len(texto) > 5:
    #print("Texto ingresado valido")
#else:
    #print("Texto invalido")

##BLOQUE2##
##ej41
#usuario = input("usuario: ")

#if usuario == "admin":
    #print("acceso permitido")
#else:
    #edad = int(input("Ingrese su edad: "))

    #if edad >= 18:
        #invitacion = input("Tiene invitacion (si/no): ")

        #if invitacion.lower() == "si":
            #print("Acceso permitido")
        #else:
            #print("Acceso denegado")
    #else:
        #print("Acceso denegado")

##ej42
#nombre = input("Ingrese su nombre: ")

#if any(c.isdigit() for c in nombre):
    #print("Datos invalidos")
#else:
    #clave = (input("Ingrese la clave: "))

    #if len(clave) < 4:
        #print("Datos invalidos")
    #else:
        #print("Datos validos")

##ej43 MAL HECHO, CODIGO DE EJEMPLO SACADO DE LA GUIA####
#datos = input("Ingrese un dato: ")

#if not datos.strip():
    #print("Campo vacio, error")

##ej44
#precio = int(input("Ingrese el precio del producto: "))

#if precio >= 1000 and precio <= 5000:
    #print("Precio dentro del rango valido")
#else:
    #print("Precio fuera del rango valido")

##ej45
#texto = input("Ingrese el texto: ")

#if not texto.startswith("#") and len(texto) % 2 == 0:
    #print("Texto valido")
#else:
    #print("Texto invalido")

##BLOQUE3##
##ej81
#intentos = 0

#while intentos < 3:
    #clave = input("Clave:")

    #if clave == "1234":
        #print("Acceso permitido")
        #break
    #intentos += 1

#if intentos == 3:
    #print("Tarjeta bloqueada")

##ej82
#total = 0

#while True:
    #num = int(input("Numero (0 para salir): "))
    #if num == 0 :
        #print("Saliendo")
        #break
    #total += num
#print(f"Suma final: {total}")

##ej83
#while True:
    #nom = input("Ingresa un nombre: ")

    #if nom.isalpha():
        #print("Nombre correcto")
        #break
    #else:
        #print("Entrada inválida. Solo se permiten letras.")

##BLOQUE4##
##ej121

#producto = int(input("Ingrese el valor neto del producto: "))

#iva = producto * 0.19
#total = producto * 1.19

# print(f"El valor de su IVA es de: {int(iva)} y el valor final es de: {int(total)}")

##ej122
#bruto = int(input("Ingrese el valor bruto: "))

#liquido = bruto * 0.1375
#liquido = bruto - liquido

#print(f"El valor liquido es de: {int(liquido)}")

##ej123

        

    
    
    







    







