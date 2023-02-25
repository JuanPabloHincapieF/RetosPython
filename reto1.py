salario, horas_extra, bonificaciones = input().split()
salario = float(salario)
horas_extra = int(horas_extra)
bonificaciones = int(bonificaciones)

hora_normal = salario/192
valor_horas_extra = (hora_normal*1.25)*horas_extra

bonificacion = 0

if bonificaciones == 1:
    bonificacion = salario * 0.05

salario_total = salario + valor_horas_extra + bonificacion
resultado = salario_total*0.915
resultado = round(resultado, 1)
print(resultado)
