##ej1
#vehiculo_pesado = 0
#vehiculo_ligero = 0

#while True:
    #try:
        #cantidad_vehiculos = int(input("Ingrese la cantidad de vehiculos: "))

        #if cantidad_vehiculos > 0:
            #break
        #else:
            #print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

    #except ValueError:
        #print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    
#for i in range(cantidad_vehiculos):
    #patente = input(f"Ingresa la patente del vehiculo numero {i+1}: ")

    #while len(patente) < 6 or " " in patente:
        #print("La patente debe contener minimo 6 caracteres y no espacios")
        #patente = input(f"Ingresa la patente del vehiculo numero {i+1}: ")

    #while True:
        #try:
            #cantidad_toneladas = int(input(f"Ingresa la capacidad de carga del vehiculo {i+1} (Toneladas):"))

            #if cantidad_toneladas > 0:
                
                #if cantidad_toneladas > 55:
                    #vehiculo_pesado += 1
                #else:
                    #vehiculo_ligero += 1
                #break

            #else:
                #print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")

        #except ValueError:
            #print("¡Error logístico! Ingresa un número entero positivo para la capacidad de carga.")

#print(f"¡La flota cuenta con {vehiculo_pesado} vehículos Pesados y {vehiculo_ligero} vehículos Ligeros! ¡Rutas asignadas!")

##ej2
#localidades = 200
#historial_ventas = 0
#capacidad_maxima = 200
#print("¡Bienvenido al sistema de gestión de localidades del Teatro Municipal!")

#while True:
    #print("1. Localidades disponibles")
    #print("2. Vender localidades")
    #print("3. Devolver localidades")
    #print("4. Historial de ventas")
    #print("5. Salir")

    #try:
        #opcion = int(input("Ingrese una opcion: "))
            
        #if opcion == 1:
            #print(f" Localidades Disponibles: {localidades}")

        #elif opcion == 2:
            #try:
                #vender_localidades = int(input("Ingrese cuantas localidades deseea vender: "))

                #if vender_localidades > 0:
                        
                    #if vender_localidades <= localidades:
                        #localidades -= vender_localidades
                        #historial_ventas += vender_localidades
                    #else:
                        #print("¡Error! No hay suficientes localidades disponibles para esta venta.")
                    
                #else:
                    #print("¡Error! La cantidad a vender debe ser un número entero mayor a cero.")
                
            #except ValueError:
                #print("¡Error! Ingrese un número entero válido para la cantidad.")

        #elif opcion == 3:
            #try:
                #localidades_devolver = int(input("Ingrese cantidad de localidades a devolver: "))

                #if localidades_devolver > 0:

                    #if localidades + localidades_devolver <= capacidad_maxima:
                        #localidades += localidades_devolver
                        #historial_ventas -= localidades_devolver
                    #else:
                        #print(f"¡Error! No se puede devolver esa cantidad. Supera la capacidad máxima del teatro ({capacidad_maxima}).")

                #else:
                    #print("¡Error! La cantidad a devolver debe ser mayor a cero.")

            #except ValueError:
                #print("¡Error! Ingrese un número entero válido para la cantidad.")

        #elif opcion == 4:
            #print(f"Historial de ventas: {historial_ventas}")
            
        #elif opcion == 5:
            #print("Gracias por utilizar nuestro software, hasta la próxima.")
            #break
        #else:
            #print("¡Error! Opción fuera de rango. Seleccione un número entre 1 y 5.")

    #except ValueError:
        #print("Ingrese solo numeros, opciones disponibles desde el 1 al 5")

##ej3
#temperatura_alta = 0
#temperatura_normales = 0

#while True:
    #try:
        #lecturas = int(input("Ingrese la cantidad de lectura de sensores: "))

        #if lecturas > 0:
            #break
        ##print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")

    #except ValueError:
        #print("¡Cantidad inválida! Ingresa un entero positivo para continuar.")
    
#for i in range(lecturas):
    #datos_lectura = input(f"Codigo de sensor {i+1}: ")

    #while len(datos_lectura) < 5 or " " in datos_lectura:
        #datos_lectura = input(f"Error numero invalidos, minimo 5 caracteres y no debe contener espacios, reingrese codigo de sensor {i+1}: ")

    #while True:
        #try:
            #temperatura_registrada = int(input("Ingrese temperatura registrada: "))

            #if -10 <= temperatura_registrada <= 50:

                #if temperatura_registrada > 30:
                    #temperatura_alta += 1
                #else:
                    #temperatura_normales += 1
                #break

            #else:
                #print("¡Error de lectura! Ingresa un número entero válido dentro del rango térmico permitido (-10 a 50).")

        #except ValueError:
            #print("¡Error de lectura! Ingresa un número entero válido dentro del rango térmico permitido (-10 a 50).")

#print(f"¡El invernadero registró {temperatura_alta} lecturas ALTAS y {temperatura_normales} lecturas NORMALES! ¡Ajuste de ventilación ejecutado!")

##ej4
#saldo_actual = 150000
#saldo_maximo = 500000
#balance_mov = 0

#print("Bienvenido a la cafeteria de la universidad")

#while True:

    #print("1. Ver saldo actual en caja")
    #print("2. Registrar egreso (Gasto de insumos)")
    #print("3. Registrar ingreso (Reposición de fondos)")
    #print("4. Ver balance neto de movimientos")
    #print("5. Cerrar caja y salir")

    #try:
        #opcion = int(input("Ingrese la opcion deseada: "))

        #if opcion == 1:
            #print(saldo_actual)
        
        #elif opcion == 2:

            #try:
                #monto_egreso = int(input("Ingrese el gasto de insumos: "))

                #if monto_egreso > 0:

                    #if monto_egreso <= saldo_actual:
                        #saldo_actual -= monto_egreso
                        #balance_mov -= monto_egreso
                    #else:
                        #print("monto ingresado no puede superar el sueldo actual")
                
                #else:
                    #print("Monto no puede ser <= 0")      

            #except ValueError:
                #print("Ingrese solo numero enteros")

        #elif opcion == 3:

            #try:
                #monto_ingreso = int(input("Ingrese la reposicion de fondos: "))

                #if monto_ingreso > 0:

                    #if monto_ingreso + saldo_actual <= saldo_maximo:
                        #saldo_actual += monto_ingreso
                        #balance_mov += monto_ingreso
                    #else:
                        #print("Operacion rechazada, no puede superar los 500000")
                
                #else:
                    #print("Monto no puede ser <= 0")
                
            #except ValueError:
                #print("Ingrese solo numero enteros")
        
        #elif opcion == 4:
            #print(f"balance neto de movimientos: {balance_mov}")
        
        #elif opcion == 5:
            #print("Gracias por utilizar nuestro software, hasta la próxima.")
            #break

        #else:
            #print("Opcion no valida, opciones disponibles del 1-5")

    #except ValueError:
        #print("Ingrese solo numeros enteros del 1-5")





