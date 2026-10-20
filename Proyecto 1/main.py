import sympy as sp

# Definimos la matriz del sistema
A = sp.Matrix([[-2, 5], [-2, 4]])

# Calculamos valores y vectores propios
eigeninfo = A.eigenvects()

print("--- RESULTADOS ---")
for val, mult, vects in eigeninfo:
    print(f"Valor propio: {val}")
    print(f"Vectores propios: {vects}\n")