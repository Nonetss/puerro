# src/puerro/commands/puerro_init.py

import subprocess
import sys

from puerro.utils.filesystem import crear_estructura_directorios, crear_makefile


def run_init(board=None):
    print("🔧 Ejecutando 'apio init'...")

    if not board:
        print("❌ Error: es necesario incluir qué board vas a usar con -b o --board.")
        print("Ejemplo: puerro init -b alhambra-ii")
        sys.exit(1)

    cmd = ["apio", "init", "-b", board]

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        print(
            "❌ Error al ejecutar 'apio init'. Asegúrate de tener apio instalado y configurado."
        )
        sys.exit(1)

    crear_estructura_directorios()
    print("✅ Proyecto inicializado con puerro 🌱")
