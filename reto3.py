filas = int(input())
base_de_datos = []
for i in range(filas):
    banos, habitaciones, trabajo, parques, precio = input().split()
    base_de_datos.append({
        'banos': int(banos),
        'habitaciones': int(habitaciones),
        'trabajo': int(trabajo),
        'parques': int(parques),
        'precio': int(precio)
    })

contador = 0
for j in range(filas):
    if base_de_datos[j]['banos'] >= 3 and base_de_datos[j]['habitaciones'] >= 4 and base_de_datos[j]['trabajo'] < 35 and base_de_datos[j]['parques'] >= 4:
        print(base_de_datos[j]['precio'])
        contador += 1
if contador == 0:
    print('NO DISPONIBLE')
