# src/puerro/commands/puerro_verilog.py

import subprocess
from pathlib import Path

from puerro.utils.config import obtener_top_module


def run_verilog():
    top = obtener_top_module()
    if not top:
        return

    src_file = Path("src") / f"{top}.vhdl"
    out_file = Path("src/build") / f"{top}.v"

    if not src_file.exists():
        print(f"❌ No se encontró el archivo VHDL: {src_file}")
        return

    print(f"🔄 Generando Verilog desde '{src_file}'...")

    cmd = [
        "yosys",
        "-m",
        "ghdl",
        "-p",
        f"ghdl {src_file} -e {top}; write_verilog {out_file}",
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Verilog generado en '{out_file}'")
    except subprocess.CalledProcessError:
        print("❌ Error al ejecutar Yosys para conversión a Verilog.")
