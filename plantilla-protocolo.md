# Plantilla de protocolo — Experimento de ubicación de producto

**Equipo:** ___ · **Integrantes:** ___ · **Fecha:** 27/10/2026

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

## 1. Pregunta e hipótesis

El producto en el pasillo principal vende más en promedioque su ubicación habitual en ventas semanales durante 4 semanas 

## 2. Unidad experimental

Semana-Tienda: Número de tiendas por cada número de semanas asociadas al experimento. (**# de tiendas x # de semanas**)

- 10 tiendas x 4 semanas = 40 unidades experimentales.

## 3. Factor, niveles y tratamiento

- **Factor** (variable manipulada): Ubicación del producto principal.
- **Niveles** (valores del factor): Ubicación en el pasillo y ubicación habitual.
- **Tratamiento** (combinación asignada): Ubicación en el pasillo durante una semana y ubicación habitual durante otra (grupo de control).

## 4. Grupo de control

La misma tienda pero con el producto dispuesto en la ubicación habitual

## 5. Aleatorización

Sorteo de 20 tiendas a cada grupo (paralelo).

- **Línea de código de la asignación (Python o R):** escribe el comando que asigna al azar tus N unidades a los dos grupos (tratamiento y control) y ejecútalo con semilla. Incluye el resultado de una corrida y explica por qué el sorteo reparte los factores desconocidos entre los grupos.

## 6. Respuesta y medición

- Variable respuesta: Ventas semanales en USD.
- Período de medición: 4 semanas.
- Quién registra y cómo (¿ciego?): Mediante el POS, ciego (vendedor no sabe si el producto está en principal o en habitual).

## 7. Factores a controlar (mínimo 4)

| Factor a controlar | Cómo se controla o registra |
|---|---|
| 1. | Clima |
| 2. | Evento local |
| 3. | Surtido / Stock |
| 4. | Cambios en el personal |

## 8. Limitaciones del diseño

- Pérdida de potencia por promociones.
- Canibalización de las tiendas.

## 9. Comparación en código (Python/R)

*Escribe `scripts/comparacion_experimento.py` (o `.R`): debe cargar `plantillas/registro_experimento.csv` y calcular el promedio de `ventas_producto` por `ubicacion`. Incluye la salida y responde:*

- ¿Qué grupo muestra mayor venta promedio en la plantilla?
El pasillo muestra 1335 USD en venta frente a 1040 USD en habitual

- ¿Por qué con 4 filas no se puede concluir nada sobre el efecto de la ubicación?
No se puede concluir porque no hay ninguna asignación real aleatoria, son muy pocos datos (4), no existe un control de temporada, ni promociones en el grupo pasillo y no hay medida de variabilidad.

- Si el experimento se ejecutara con tu protocolo, ¿qué le faltaría a este análisis para ser justo?
´´´
import pandas as pd
import numpy as np

tiendas = ["Quito Norte", "Quito Sur", "Guayaquil Centro", "Guayaquil Norte",
            "Cuenca Centro", "Cuenca Sur", "Ambato Centro", "Manta", "Loja", "Machala"]

semanas = [1, 2, 3, 4]

#Sorteo de la condicion inicial
rng = np.random.default_rng(1234597) ##permite generar rangos aleatorios bajo condiciones
primera = rng.choice(["pasillo_principal", "habitual"], size=len(tiendas))
filas = []

for tienda, cond in zip(tiendas, primera):
    otra = "habitual" if cond == "pasillo_principal" else "pasillo_principal"
    for s in semanas:
        filas.append({"tienda": tienda, "semana": s,
                     "ubicacion": cond, if s&2 == 1 else otra})
´´´