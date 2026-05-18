##ej1
#for numero in range(1, 21):
    #if numero % 2 == 0 and numero % 5 == 0:
        #print(f"El numero {numero} es par y multiplo de 5")
    #elif numero % 2 != 0 and numero % 5 == 0:
        #print(f"El numero {numero} es impar y multiplo de 5")
    #elif numero % 2 == 0:
        #print(f"El numero {numero} es par")
    #else:
        #print(f"El numero {numero} es impar")

##ej2
#notas = [4.5, 3.8, 2.9, 4.2, 3.5]
#suma = 0


#for nota in notas:
    #suma = suma + nota

#promedio = suma / len(notas)

#if promedio >= 4.0:
    #print(f"Aprueba con {promedio:0.1f}")
#elif promedio >= 3.0 and promedio < 4.0:
    #print(f"Habilita con {promedio:0.1f}")
#else:
    #print(f"Reprueba con {promedio:0.1f}")

##ej3
#numeros = [8, -3, 0, 12, -7, 0, 5, -1]
#positivos = 0
#negativos = 0
#ceros = 0

#for numero in numeros:
    #if numero > 0:
        #positivos += 1
    #elif numero < 0:
        #negativos += 1
    #else:
        #ceros += 1

#print(f"Positivos: {positivos}")
#print(f"Negativos: {negativos}")
#print(f"Ceros: {ceros}")

##ej4
#for numero in range(1, 51):
    #if (numero % 3 == 0 or numero % 7 == 0) and not (numero % 3 == 0 and numero % 7 == 0):
        #print(numero) 

##ej5
#frase = "Python es poderoso"
#vocales = 0
#consonantes = 0
#espacios = 0

#for letra in frase.lower():
    #if letra in "aeiou":
        #vocales += 1
    #elif letra == " ":
        #espacios += 1
    #else:
        #consonantes += 1

#print(f"Vocales: {vocales}")
#print(f"Consonantes: {consonantes}")
#print(f"Espacios: {espacios}")

##ej6
#edades = [8, 15, 22, 67, 13, 40]

#for edad in edades:
    #if edad < 12:
        #print(f"{edad} -> Niño")
    #if edad >= 12 and edad < 18:
        #print(f"{edad} -> Adolescente")
    #elif edad >= 18 and edad < 60:
        #print(f"{edad} -> Adulto")
    #else:
        #print(f"{edad} -> Adulto mayor")

##ej7
#for numero in range(2, 31):
    #es_primo = True
    #for divisor in range(2, numero):
        #if numero % divisor == 0:
            #es_primo = False
            #break
    #if es_primo:
        #print(numero, "es primo")
    #else:
        #print(numero, "no es primo")

##ej8
#numero = int(input("Ingresa un numero: "))

#if numero > 0:
    #for i in range(1, 11):
        #resultado = numero * i
        #print(f"{numero} x {i} = {resultado}")
#else:
    #print("El numero debe ser mayor que cero")

##ej9


##ej10
#precios = [35, 50, 120, 89, 210]
#for precio in precios:
    #if precio > 100:
        #total = precio * 0.80
        #print(precio, "-> descuento 20% ->", total)
    #elif precio >= 50:
        #total = precio * 0.90
        #print(precio, "-> descuento 10% ->", total)
    #else:
        #print(precio, "-> sin descuento ->", precio)