#MANEJO DE TUPLAS
primos = (2,3,5,7,11,13)
pares = [2,4,6,8,19]
dias = ("lunes", "martes", "miercoles", "jueves", "viernes")

primos2 = list(primos)
primos2.pop()
primos = tuple(primos2)
primosordenados = sorted(primos, reverse=True)
print(primosordenados)

print(dias[2])
print(max(primos))
print(max(pares))