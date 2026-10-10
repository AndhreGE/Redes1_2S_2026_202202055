import sympy as sp

# Definimos la matriz del sistema
A = sp.Matrix([[5, 3, 3], [3, 5, 3], [-5, -5, -3]])

# Calculamos valores y vectores propios
eigeninfo = A.eigenvects()
for val, mult, vects in eigeninfo:
    print(f"Valor propio: {val}, Vectores propios: {vects}")