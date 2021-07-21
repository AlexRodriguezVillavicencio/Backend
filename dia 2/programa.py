#INGRESE EL NUMERO DE NOTAS A EVALUAR
#NOTA MAX, NOTA MIN, PROMEDIO

notas = []
totalNotas = int(input("cuentas notas deseas evaluar: "))
promedio = 0
for n in range(1,totalNotas + 1):
    nota = int(input("nota " + str(n) + ": "))
    promedio += nota
    notas.append(nota)
promedio = promedio / totalNotas
print(notas)
print(max(notas))
print(min(notas))
print(promedio)