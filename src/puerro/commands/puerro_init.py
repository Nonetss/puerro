# src/puerro/commands/init.py

import subprocess

from puerro.utils.filesystem import crear_estructura_directorios, crear_makefile


def run_init(board=None):
    print("🔧 Ejecutando 'apio init'...")
    cmd = ["apio", "init"]
    if board:
        cmd += ["-b", board]
    subprocess.run(cmd, check=True)

    crear_estructura_directorios()
    crear_makefile()
    print("✅ Proyecto inicializado con puerro 🌱")
