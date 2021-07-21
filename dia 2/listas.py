#TRABAJO CON LISTAS
primos = [2,3,5,7,11,13]
dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]


print(dias[1:4])
print(primos)
dias.pop()
print(dias)
del primos[3]
print(primos)
primos.insert(3,7)
print(primos)

for x in dias:
    print(x)

for i in range(len(primos)):
    print(primos[i])