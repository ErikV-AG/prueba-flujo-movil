"""Lee datos.csv e imprime el total de alumnos y el avance promedio por curso."""

import csv
from collections import defaultdict
from pathlib import Path

RUTA_CSV = Path(__file__).with_name("datos.csv")


def main():
    total_alumnos = 0
    avances = defaultdict(list)

    with RUTA_CSV.open(newline="", encoding="utf-8") as archivo:
        for fila in csv.DictReader(archivo):
            total_alumnos += int(fila["alumnos"])
            avances[fila["curso"]].append(float(fila["avance_pct"]))

    print(f"Total de alumnos: {total_alumnos}")
    print()
    print("Avance promedio por curso:")
    for curso in sorted(avances):
        valores = avances[curso]
        print(f"  {curso}: {sum(valores) / len(valores):.1f}%")


if __name__ == "__main__":
    main()
