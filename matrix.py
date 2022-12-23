import numpy as np
from fractions import Fraction

def matrix_properties(matrix):
  # Calculer le nombre de lignes et de colonnes de la matrice
  num_rows = len(matrix)
  num_cols = len(matrix[0])

  # Calculer la transposée de la matrice
  transpose = [[matrix[j][i] for j in range(num_rows)] for i in range(num_cols)]

  # Calculer le déterminant de la matrice
  if num_rows != num_cols:
    determinant = None
  elif num_rows == 2:
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  else:
    determinant = 0
    for i in range(num_cols):
      submatrix = [row[:i] + row[i+1:] for row in matrix[1:]]
      determinant += (-1) ** i * matrix[0][i] * matrix_properties(submatrix)['determinant']

  # Calculer l'inverse de la matrice
  if determinant == 0:
    inverse = None
  elif num_rows == 2:
    inverse = [[matrix[1][1]/determinant, -matrix[0][1]/determinant],
               [-matrix[1][0]/determinant, matrix[0][0]/determinant]]
  else:
    inverse = [[0 for i in range(num_cols)] for j in range(num_rows)]
    for i in range(num_rows):
      for j in range(num_cols):
        submatrix = [row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]]
        inverse[i][j] = ((-1) ** (i+j)) * matrix_properties(submatrix)['determinant'] / determinant

  # Convertir la matrice en un objet numpy.array pour pouvoir utiliser la fonction eig
  matrix = np.array(matrix)

  # Calculer les valeurs propres et les vecteurs propres de la matrice
  eigenvalues, eigenvectors = np.linalg.eig(matrix)

  # Convertir les valeurs propres et les vecteurs propres en fractions en entier
  eigenvalues = [Fraction(x).limit_denominator() for x in eigenvalues]
  eigenvectors = [[Fraction(x).limit_denominator() for x in row] for row in eigenvectors]
  # Renvoyer les résultats sous forme de dictionnaire
  return {'transpose': transpose,
          'determinant': determinant,
          'inverse': inverse,
          'eigenvalues': eigenvalues,
          'eigenvectors': eigenvectors}


def spectral_projector(matrix, eigenvalues, eigenvectors):
  # Calculer le nombre de lignes et de colonnes de la matrice
  num_rows = len(matrix)
  num_cols = len(matrix[0])

  # Convertir la matrice et les vecteurs propres en objets numpy.array
  matrix = np.array(matrix)
  eigenvectors = np.array(eigenvectors)

  # Créer la matrice de projection en multipliant chaque vecteur propre par sa valeur propre
  projector = np.zeros((num_rows, num_cols))
  for i in range(num_rows):
    projector += eigenvalues[i] * np.outer(eigenvectors[:,i], eigenvectors[:,i])

  # Convertir chaque élément de la matrice de projection en fraction
  projector = [[Fraction(x).limit_denominator() for x in row] for row in projector]

  return projector


# Exemple d'utilisation de la fonction
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]
#print(matrix_properties(matrix))
print("La matrice de base est " + str(matrix))
result = matrix_properties(matrix)
transpose = result['transpose']
determinant = result['determinant']
inverse = result['inverse']
print("Transpose : ")
print(transpose)
print("determinant : ")
print(determinant)
print("inverse: ")
print(inverse)
# Afficher chaque clé et sa valeur sur une ligne différente
eigenvalues = result['eigenvalues']
eigenvectors = result['eigenvectors']
print("Valeurs propres :")
for eigenvalue in eigenvalues:
  print(f"  - {eigenvalue.__str__()}")
print("Vecteurs propres :")
for i, eigenvector in enumerate(eigenvectors):
  print(f"  - Valeur propre {eigenvalues[i].__str__()}: {[x.__str__() for x in eigenvector]}")

# Exemple d'utilisation de la fonction
#matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
eigenvalues, eigenvectors = np.linalg.eig(matrix)
projector = spectral_projector(matrix, eigenvalues, eigenvectors)
#print(projector)
print("Projection specale")
for row in projector:
  print("[", end=" ")
  for x in row:
    print(x, end=" ")
  print("]")
