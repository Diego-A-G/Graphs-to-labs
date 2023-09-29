import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos de longitud del péndulo y período de oscilación (reemplaza estos datos con los tuyos)
longitudes = np.array([0.5, 1.0, 1.5, 2.0, 2.5])  # Longitudes en metros
periodos = np.array([1.57, 2.22, 2.92, 3.49, 3.96])  # Periodos en segundos

# Calcular la aceleración debida a la gravedad (g) usando regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(np.sqrt(longitudes), periodos)
g = (4 * np.pi**2) / (slope**2)

# Calcular la propagación del error
delta_L = np.std(longitudes)
delta_T = np.std(periodos)
delta_g = (2 * g * delta_L) / np.mean(longitudes)

# Imprimir resultados
print(f"Aceleración debida a la gravedad (g): {g} m/s^2")
print(f"Error en g: +/- {delta_g} m/s^2")

# Graficar los datos y la línea de regresión
plt.scatter(np.sqrt(longitudes), periodos, label='Datos')
plt.plot(np.sqrt(longitudes), intercept + slope*np.sqrt(longitudes), color='red', label='Regresión lineal')
plt.xlabel('Raíz Cuadrada de la Longitud (m^0.5)')
plt.ylabel('Periodo (s)')
plt.legend()
plt.show()
