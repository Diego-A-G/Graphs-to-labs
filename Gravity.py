import numpy as np
import matplotlib.pyplot as plt

# Datos de longitud del péndulo (metros) y tiempo de oscilación (s)
longitudes = np.array([0.175, 0.225, 0.275, 0.325, 0.375, 0.425, 0.475])  # Longitudes en metros
tiempos_oscilacion = np.array([0.8396, 0.9520, 1.0525, 1.1442, 1.2290, 1.3084, 1.3832])  # Tiempos de oscilación en segundos

# Calcular el período al cuadrado (T^2)
periodo_cuadrado = tiempos_oscilacion ** 2

# Realizar una regresión lineal para encontrar la pendiente (4*pi^2*L/g)
pendiente, _ = np.polyfit(longitudes, periodo_cuadrado, 1)

# Calcular la aceleración debida a la gravedad (g) a partir de la pendiente
g = (4 * (np.pi ** 2) * longitudes) / pendiente

# Calcular el valor promedio de la gravedad
g_promedio = np.mean(g)

# Crear una gráfica de dispersión de los datos
plt.scatter(longitudes, periodo_cuadrado, label='Datos')

# Calcular los valores estimados de T^2 utilizando la pendiente encontrada
periodo_cuadrado_estimado = pendiente * longitudes

# Dibujar la línea de regresión
plt.plot(longitudes, periodo_cuadrado_estimado, color='red', label='Regresión Lineal')

# Etiquetas y leyenda
plt.xlabel('Longitud del Péndulo (m)')
plt.ylabel('Período al Cuadrado (s^2)')
plt.legend()

# Mostrar la gráfica
plt.show()

# Imprimir el valor promedio de la gravedad (g)
print(f'El valor promedio de la gravedad (g) es: {g_promedio} m/s^2')
