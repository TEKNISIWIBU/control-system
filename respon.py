import control as ct
import numpy as np
import matplotlib.pyplot as plt
    
numerator = [1]
denominator = [1, 0.1]
G = ct.tf(numerator, denominator)
    
time = np.linspace(0, 10, 100) # Time vector
t, response = ct.step_response(G, time)
        
plt.plot(t, response)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('Step Response')
plt.grid()
plt.show()