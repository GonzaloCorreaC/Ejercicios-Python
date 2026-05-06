##ej1
#edad = int(input("Ingrese su edad: "))

#if edad < 12:
    #print("Niño: pasa gratis")
#elif edad <= 17:
    #print("Adolescente: media tarifa")
#elif edad <= 64:
    #print("Adulto: taria completa")
#else:
    #print("Adulto mayor: media tarifa")

##ej2
#precio = int(input("Ingrese el precio del producto: "))
#socio = input("¿Es socio? (s/n): ").lower()

#if precio > 50000:

    #if socio =="s":
        #descuento = 0.20
    #else:
        #descuento = 0.10

#elif precio <= 50000:

    #if socio == "s":
        #descuento = 0.05
    #else: 
        #descuento = 0

#else:
    #descuento = 0

#final = precio * (1 - descuento)
#print(f"Final: ${final:.2f}")

##ej3
#base = 2000

#horas = int(input("Horas de estadia: "))
#vehiculo = (input("Tipo de vehiculo : 1=auto, 2=moto, 3=camion"))

#f horas > 12:
    #print("Maximo 12 horas permitidas")
#else:
    #if vehiculo == "1":

        #if horas >= 3:
            #descuento = 0.10
        #else: 
            #descuento = 0

    #elif vehiculo == "2":
        #descuento = 0.50

    #elif vehiculo == "3":
        #descuento = -0.30
    #else:
        #descuento = 0

#total = (base * horas) 
#total_final = total * (1 - descuento)

#print(f"Horas: {horas}")
#print(f"Tipo: {vehiculo}")
#print(f"Total: ${total_final:0.0f}")

##ej5
#base = 30000
#inscripcion = 10000

#meses = int(input("Cuantos meses lleva contratado: "))
#plan = input("Tipo de plan: 1=basico, 2=estandar, 3=premium")

#if meses >= 6:

    #if plan == "1" or plan == "2":
        #descuento = 0.15
    #else:
        #descuento = 0.25

#elif 3 <= meses <= 5:
    #descuento = 0.08

#else:
    #descuento = 0

#if (plan == "2" or plan == "3") and meses >= 6:
    #inscripcion = 0

#elif plan == "2" or plan == "3":
    #inscripcion = inscripcion * 0.50

#else:
    #inscripcion = inscripcion

#mensualidad = base * (1 - descuento)


#print(f"Meses: {meses}")
#print(f"Plan: {plan}")
#print(f"Mensualidad: ${mensualidad:0.0f}  Inscripcion: ${inscripcion:0.0f}")



