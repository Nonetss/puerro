# src/puerro/commands/puerro_build.py

import shutil
import subprocess
from pathlib import Path


def run_build():
    build_dir = Path("src/build")
    build_dir.mkdir(parents=True, exist_ok=True)

    # Copiar apio.ini a src/build/
    shutil.copy("apio.ini", build_dir / "apio.ini")
    print(f"📋 Copiado apio.ini → {build_dir / 'apio.ini'}")
    shutil.copy("pins.pcf", build_dir / "pins.pcf")
    print(f"📋 Copiado pins.pcf → {build_dir / 'pins.pcf'}")

    # Ejecutar 'apio build' dentro de src/build
    print("🔧 Ejecutando 'apio build' dentro de src/build...")
    try:
        subprocess.run(["apio", "build"], cwd=build_dir, check=True)
        print("✅ Build completado. Artefactos en src/build/")
    except subprocess.CalledProcessError:
        print("❌ Error durante el build con APIO.")
