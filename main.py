# INSTRUCCIONES:
# Corregir la implementación del algoritmo de Euclides

# 1.- Damos valores iniciales
print("Valores iniciales")
A = 270
B = 192
print(A)
print(B)
# 2.- Ciclo del algoritmo
for i in range(5):
  print("Iteración " + str(i))
  R = A % B
  print("R = " + str(R))

  A = B
  B = R
  print("A = " + str(A))
  print("B = " + str(B))
# Resultados (asignar el resultado del M.C.D. a la variable M)
print("El M.C.D. es = " + str(M))
