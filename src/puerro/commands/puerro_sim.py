# src/puerro/commands/puerro_sim.py

import subprocess
from pathlib import Path

from puerro.utils.config import obtener_top_module


def run_sim():
    entidad = obtener_top_module()
    if not entidad:
        return

    vcd_path = Path("wave") / f"{entidad}.vcd"

    print(f"🔧 Elaborando entidad '{entidad}'...")
    try:
        subprocess.run(["ghdl", "-e", entidad], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error al elaborar con GHDL")
        return

    print(f"▶️ Ejecutando simulación y generando VCD en '{vcd_path}'...")
    try:
        subprocess.run(["ghdl", "-r", entidad, f"--vcd={vcd_path}"], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error al simular con GHDL")
        return

    if not vcd_path.exists():
        print("❌ Archivo VCD no generado.")
        return

    print("📊 Abriendo GTKWave...")
    try:
        subprocess.run(["gtkwave", str(vcd_path)])
    except FileNotFoundError:
        print("❌ GTKWave no está instalado o no se encuentra en el PATH.")
