import control as ct
import numpy as np
import matplotlib.pyplot as pt

A = np.array([[1, 2, 1], [0, 1, 3], [1, 1, 1]])
B = np.array([[1], [0], [1]])

sys = ct.ss(A, B, np.eye(3), np.zeros((3, 1)))
G = ct.ss2tf(sys)
print("Hasil perkalian matriks A dan B:")
print(sys)
print(G)