# Windchill es cuando en hace frio, el viento se siente incluso mas frio, porque el movimiento del aire incrementa la capacidad de enfriar

#Constantes
cteUno = 13.12
cteDos = 0.6215
cteTres = -11.37
cteCuatro = 0.3965
cteCinco = 0.16
Tmax = 10
Vmin = 4.8
#Pido datos
Ta = float(input('Temperatura del aire en grados celcius: '))
V = float(input('Velocidad del viento en kilometros por hora: '))

#Hago los calculos
if Ta<Tmax and V>Vmin:
    WCI = cteUno + cteDos*Ta + cteTres*(V**cteCinco) + cteCuatro*Ta*(V**cteCinco)
    #Imprimo los resultados
    print('El indice es igual a: '+ str(round(WCI,3)))
else:
    print('Wind Chill no es valido para temperaturas mayores a 10 grados o velocidades menores a 4.8km/h')