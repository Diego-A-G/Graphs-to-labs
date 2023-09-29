import matplotlib.pyplot as plt

# Datos
masas = [80, 90, 100, 110, 120, 150]
longitudes = [16.8, 18, 18.8, 19.3, 20.1, 23.1]

# Crear la gráfica
plt.figure(figsize=(8, 6))
plt.scatter(masas, longitudes, color='blue', marker='o', label='Puntos')  # Etiqueta para los puntos
plt.plot(masas, longitudes, color='red', linestyle='-', label='Línea')  # Agregar la línea
plt.title('Longitud vs. Masa')
plt.xlabel('Masa (kg)')
plt.ylabel('Longitud (cm)')

# Mostrar la gráfica
plt.grid(True)
plt.legend()  # Mostrar leyenda
plt.show()
