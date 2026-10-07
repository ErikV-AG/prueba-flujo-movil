# prueba-flujo-movil

## Contenido

- `index.html`: página autocontenida con la tarjeta "Estado del sistema", que muestra la hora de Ciudad de México, se actualiza cada segundo e incluye un botón para copiar la hora al portapapeles. Ábrela directamente en el navegador.
- `datos.csv`: datos de ejemplo con las columnas `curso`, `alumnos` y `avance_pct`.
- `resumen.py`: script que lee `datos.csv` e imprime el total de alumnos y el avance promedio por curso.

## Cómo correr el script

Requisitos: Python 3.6 o superior. No necesita dependencias externas (solo la librería estándar).

```bash
python3 resumen.py
```

El script busca `datos.csv` en la misma carpeta que `resumen.py`, así que puedes ejecutarlo desde cualquier directorio.

Salida esperada:

```
Total de alumnos: 287

Avance promedio por curso:
  Historia: 61.0%
  Inglés: 87.5%
  Matemáticas: 74.5%
  Programación: 79.0%
  Química: 70.0%
```
