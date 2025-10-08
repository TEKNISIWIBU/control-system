import scipy.signal as signal
import control as ct
import numpy as np

# Define numerator and denominator coefficients
numerator = np.array([4])  # Represents 1 in the numerator
denominator = np.array([3, -2, 1]) # Represents s + 0.1 in the denominator

# Create the transfer function object
#tidak menampilkan bentuk dari transfer function
#F = signal.TransferFunction(numerator, denominator)
#print(F)
#menampilkan bentuk dari transfer function
G = ct.tf(numerator, denominator)
print('H(s) = ' ,G)