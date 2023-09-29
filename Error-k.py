import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Datos de masa y período de oscilación (reemplaza estos datos con los tuyos)
masas = np.array([0.1, 0.2, 0.3, 0.4, 0.5])  # Masas en kg
periodos = np.array([1.0, 1.4, 1.7, 2.0, 2.3])  # Periodos en segundos

# Calcular la constante de elasticidad (k) usando regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(masas, periodos)
k = 4 * np.pi**2 / slope

# Calcular la propagación del error
delta_m = np.std(masas)
delta_T = np.std(periodos)
delta_k = (8 * np.pi**2 * delta_m) / (slope**2)

# Imprimir resultados
print(f"Constante de elasticidad (k): {k} N/m")
print(f"Error en k: +/- {delta_k} N/m")

# Graficar los datos y la línea de regresión
plt.scatter(masas, periodos, label='Datos')
plt.plot(masas, intercept + slope*masas, color='red', label='Regresión lineal')
plt.xlabel('Masa (kg)')
plt.ylabel('Periodo (s)')
plt.legend()
plt.show()
