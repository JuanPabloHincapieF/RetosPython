distancia, velocidad_maxima, tiempo = input().split()
distancia = int(distancia)
velocidad_maxima = int(velocidad_maxima)
tiempo = int(tiempo)
velocidad = ((distancia/1000)*3600)/tiempo
if distancia >= 0 and velocidad_maxima >= 0 and tiempo >= 0:
    if velocidad < velocidad_maxima:
        print('OK')
    elif velocidad < (velocidad_maxima*1.20):
        print('MULTA')
    elif velocidad >= (velocidad_maxima*1.20):
        print('CURSO SENSIBILIZACION')
    else:
        print('ERROR')
else:
    print('ERROR')
