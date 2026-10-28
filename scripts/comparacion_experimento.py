# comparacion_experimento.py — Comparación de grupos (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/comparacion_experimento.py
import pandas as pd
# TODO 1: carga plantillas/registro_experimento.csv con pandas
df = pd.read_csv('plantillas/registro_experimento.csv')
print(df.head())


# TODO 2: calcula e imprime el promedio de ventas_producto por ubicacion
print(df.groupby('ubicacion')['ventas_producto'].mean())


# TODO 3: imprime el número de registros por grupo (value_counts)
print(df['ubicacion'].value_counts())


# TODO 4: escribe 2–3 líneas de interpretación (sección 9 de la plantilla):
#         por qué con 4 filas no se puede concluir y qué le faltaría al análisis
'''
No se puede concluir porque no hay ninguna asignación real aleatoria, son muy pocos datos (4), no existe un control de temporada, 
ni promociones en el grupo pasillo y no hay medida de variabilidad.
'''