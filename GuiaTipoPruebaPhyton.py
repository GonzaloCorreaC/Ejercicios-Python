##ej1
#edad = int(input("Ingrese su edad: "))

#if edad >= 18:
    #print("Eres mayor de edad")
#else:
    #print("Eres menor de  edad")

#edad_actualizada = edad + 5
#print(f"Tu edad en 5 años sera de, {edad_actualizada} años")

##ej2
#num1 = int(input("Ingresa el primer numero: "))
#num2 = int(input("Ingresa el segundo numero: "))

#suma = num1 + num2
#resta = num1 - num2
#multiplicacion = num1 * num2

#print(f"El resultado de la suma es de: {suma}")
#print(f"El resultado de la resta es de: {resta}")
#print(f"El resultado de la multiplicacion es de: {multiplicacion}")

#if num2 != 0:
    #division_entera = num1 // num2
    #residuo = num1 % num2
    #print(f"El resultado de la division entera es de: {division_entera}")
    #print(f"El resultado del residuo es de: {residuo}")
#else:
    #print("Error no se puede dividir por cero")

##ej3
#contraseña = input("Ingrese una contraseña: ")
#contraseña = contraseña.lower()
#acceso = False

#if contraseña == "python123":
    #print("Acceso concedido")
    #acceso = True
#else:
    #print("Acceso denegado")

#print(f"Variable acceso: {acceso}")

##ej4
#num = int(input("Ingresa un numero: "))

#if num > 0:
    #cuadrado = num ** 2
    #print(f"El cuadrado del numero es de: {cuadrado}")
#elif num < 0:
    #print("Numero negativo, no se calcula el cuadrado")
#else:
    #print("Numero ingresado fue cero")

##ej5
#valor1 = input("Ingrese True or False: ")
#valor2 = input("Ingrese True or False: ")
#valor1 = valor1.lower()
#valor2 = valor2.lower()

#if valor1 == "true":
    #valor1 = True
#else:
    #valor2 = False

#if valor2 == "true":
    #valor2 = True
#else:
    #valor2 = False

#operacion_and = valor1 and valor2
#operacion_or = valor1 or valor2

##ej6
#calificacion1 = int(input("Ingrese la nota: "))
#calificacion2 = int(input("Ingrese la nota: "))
#calificacion3 = int(input("Ingrese la nota: "))

#promedio = (calificacion1 + calificacion2 + calificacion3) / 3

#if promedio >= 70:
    #estado = "Aprobado"
#elif promedio >= 50 and promedio <= 69:
    #estado = "Recuperacion"
#else:
    #estado = "Reprobado"

#print(F"El promedio de las tres notas es de: {promedio}")
#print(f"El estado de la nota es de: {estado}")

##ej7
#nombre = input("Ingrese su nombre: ")
#año_nacimiento = int(input("Ingrese su año de nacimiento: "))

#edad = 2025 - año_nacimiento

#if edad >= 18:
    #print(f"Bienvenido {nombre}")
#else:
    #print("Acceso denegado")

##ej8
#num = int(input("Ingrese un numero: "))

#if num % 2 == 0 and num > 10:
    #print("Numero par y mayor que 10")
#elif num % 2 == 0 and num <= 10:
    #print("Numero par menor o igual a 10")
#else:
    #print("Numero impar")

##ej9
#num = int(input("Ingresa un numero: "))

#num_actualizacion = num + 10
#print(f"Numero actualizado: {num_actualizacion}")

#if num_actualizacion % 3 == 0 and num_actualizacion % 5 == 0:
    #print("El numero es multiplo de 3 y 5")
#else:
    #print("No es multiplo de 3 y 5 al mismo tiempo")

##ej10
#caracter = input("Ingresa un caracter: ")
#caracter = caracter.lower()

#if len(caracter) != 1:
    #print("Debe ser solo un caracter")
#else:
    #if caracter in "aeiou":
        #print("Es vocal")
    #elif caracter.isalpha():
        #print("Es consonante")
    #else:
        #print("No es letra")

##ej11
#base = int(input("Ingrese la base del rectangulo: "))
#altura = int(input("Ingrese la altura del rectangulo: "))

#area = base * altura

#if area > 100:
    #print("Rectangulo grande")
#else:
    #print("Rectangulo pequeño")

##ej12
#num1 = int(input("Ingresa el primer numero: "))
#num2 = int(input("Ingresa el segundo numero: "))

#num1 = num1 + num2
#num2 = num2 - 3

#if num1 > num2:
    #print(f"El primer numero actualizado es mayor: {num1} > {num2}")
#elif num2 > num1:
    #print(f"El segundo numero actualizado es mayor: {num2} > {num1}")
#else:
    #print("Son iguales")

##ej13
#texto = input("Ingrese un texto: ")

#if len(texto) > 10:
    #texto = texto.upper()
#else:
    #texto = texto.lower()

#print(texto)

##ej14
#num = int(input("Ingresa un numero (1-7): "))

#if num == 1:
    #dia = "Lunes"
#elif num == 2:
    #dia = "Martes"
#elif num == 3:
    #dia = "Miercoles"
#elif num == 4:
    #dia = "Jueves"
#elif num == 5:
    #dia = "Viernes"
#elif num == 6:
    #dia = "Sabado"
#elif num == 7:
    #dia = "Domingo"
#else:
    #dia = "Numero invalido"

#print(dia)

##ej15
#num1 = int(input("Ingresa el primer numero: "))
#num2 = int(input("Ingresa el segundo numero: "))

#suma = num1 + num2
#resta = num1 - num2
#multiplicacion = num1 * num2

#print("1=suma, 2=resta, 3=multiplicación")
#opt = int(input("Que operacion quiere ver: "))

#if opt == 1:
    #print(f"Suma: {suma}")
#elif opt == 2:
    #print(f"Resta: {resta}")
#elif opt == 3:
    #print(f"Multiplicacion: {multiplicacion}")
#else:
    #print("Numero invalido")

##ej16
#producto = input("Nombre producto: ")
#precio = int(input("Ingresa el precio: "))

#if precio > 1000:
    #precio = precio * 0.85
#else: 
    #precio = precio * 0.95

#print(f"El precio final es de: {int(precio)}")

##ej17
#num1 = int(input("Ingresa el primer numero: "))
#num2 = int(input("Ingresa el segundo numero: "))
#num3 = int(input("Ingresa el tercer numero: "))

#positivos = 0

#if num1 > 0:
    #positivos = positivos + 1
#if num2 > 0:
    #positivos = positivos + 1
#if num3 > 0:
    #positivos = positivos + 1

#if positivos >= 2:
    #resultado = True
#else:
    #resultado = False

#print(f"¿Al menos dos son positivos? {resultado}")

##ej18
#año = int(input("Ingresa un año: "))

#if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    #print(f"{año} es bisiesto")
#else:
    #print(f"{año} no es bisiesto")

##ej19
#num = int(input("Numero: "))


#if num < 0:
    #num = -num

#print(f"Valor absoluto: {num}")

#veces_cabe = num // 3
#print(f"El 3 cabe {veces_cabe} veces en {num}")

##ej20
#nombre = input("Nombre: ")
#edad = int(input("Edad: "))
#ciudad = input("Ciudad: ")
#horas = float(input("Horas trabajadas: "))
#valor_hora = float(input("Valor por hora: "))

#salario = horas * valor_hora
#print(f"Salario bruto: {salario}")

#if salario > 1000:
    #salario = salario * 0.80
    #print("Se aplico impuesto del 20%")

#if edad < 18 or edad > 65:
    #salario = salario * 0.95
    #print("Se aplico descuento especial del 5%")

#print("Resumen")
#print(f"Nombre: {nombre}")
#print(f"Ciudad: {ciudad}")
#print(f"Edad: {edad}")
#print(f"Salario neto final: {salario}")

