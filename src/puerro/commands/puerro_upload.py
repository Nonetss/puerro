# src/puerro/commands/puerro_upload.py

import subprocess
from pathlib import Path


def run_upload():
    build_dir = Path("src/build")
    apio_ini = build_dir / "apio.ini"

    if not apio_ini.exists():
        print(
            "❌ No se encontró apio.ini en src/build. Ejecuta 'puerro build' primero."
        )
        return

    print("📤 Subiendo diseño a la FPGA desde 'src/build/'...")
    try:
        subprocess.run(["apio", "upload"], cwd=build_dir, check=True)
        print("✅ Subida completada con éxito.")
    except subprocess.CalledProcessError:
        print("❌ Error al subir con APIO.")
