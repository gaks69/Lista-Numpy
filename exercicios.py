import numpy as np

# Exercício 1
array_1d = np.arange(1, 11)  # Cria um array de 1 a 10
array_2d = array_1d.reshape(2, 5)  # Transforma em array 2x5
print("Exercício 1:\n", array_2d)




# Exercício 6
array_rand = np.random.randint(1, 101, size=20)  # Array aleatório entre 1 e 100
array_rand[array_rand > 50] = 0  # Substitui valores maiores que 50 por 0
print("\nExercício 6:\n", array_rand)




# Exercício 9
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
x_new = [1.5, 2.5, 3.5, 4.5]
y_new = np.round(np.interp(x_new, x, y), 2)  # Interpola valores de y e arredonda
print("\nExercício 9:\n", y_new)



# Exercício 12
array_linspace = np.round(np.linspace(0, 10, 50), 2)  # Array com 50 valores igualmente espaçados entre 0 e 10, arredondado
array_arange = np.round(np.arange(0, 10.2, 0.2), 2)  # Array com valores de 0 a 10 incrementando de 0.2, arredondado
print("\nExercício 12 (linspace):\n", array_linspace)
print("\nExercício 12 (arange):\n", array_arange)



# Exercício 14
array_14 = np.random.randint(0, 101, size=15)  # Array de tamanho 15 entre 0 e 100
pares = array_14[array_14 % 2 == 0]  # Seleciona números pares
array_14[array_14 % 2 != 0] = -1  # Substitui números ímpares por -1
print("\nExercício 14 (pares):\n", pares)
print("\nExercício 14 (modificado):\n", array_14)



# Exercício 15
matriz_15 = np.random.randint(1, 10, size=(3, 3))  # Matriz 3x3
matriz_flatten = matriz_15.flatten()  # Redimensiona para 1x9
matriz_reshaped = matriz_flatten.reshape(9, 1)  # Redimensiona para 9x1
print("\nExercício 15 (matriz original):\n", matriz_15)
print("\nExercício 15 (1x9):\n", matriz_flatten)
print("\nExercício 15 (9x1):\n", matriz_reshaped)



# Exercício 18
coeficientes = [1, -4, 6, -24]  # Coeficientes do polinômio p(x) = x^3 - 4x^2 + 6x - 24
raizes = np.round(np.roots(coeficientes), 2)  # Raízes do polinômio, arredondadas
valor_p2 = np.round(np.polyval(coeficientes, 2), 2)  # Valor de p(x) para x = 2, arredondado
print("\nExercício 18 (raízes):\n", raizes)
print("\nExercício 18 (p(2)):\n", valor_p2)





# Exercício 30
x_30 = np.linspace(0, 10, 20)  # Valores de x
ruido = np.random.normal(0, 1, size=20)  # Ruído normal
y_30 = 2 * x_30 + 3 + ruido  # Dados simulados
# Regressão linear usando álgebra matricial
X = np.vstack([x_30, np.ones_like(x_30)]).T  # Matriz de design
coeficientes_reg = np.round(np.linalg.lstsq(X, y_30, rcond=None)[0], 2)  # Coeficientes (a, b), arredondados
print("\nExercício 30 (coeficientes da regressão):\n", coeficientes_reg)

