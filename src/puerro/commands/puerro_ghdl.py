# src/puerro/commands/ghdl.py

import glob
import subprocess
from pathlib import Path


def analizar_archivos(ruta, nombre=""):
    archivos = sorted(glob.glob(f"{ruta}/*.vhdl"))
    if not archivos:
        print(f"⚠️  No se encontraron archivos en {ruta}/")
        return True

    if nombre:
        print(f"🔹 Analizando {nombre}/")
    for archivo in archivos:
        print(f"  → {archivo}")
        try:
            subprocess.run(["ghdl", "-a", "--workdir=src/build", archivo], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Error al analizar: {archivo}")
            return False
    return True


def run_ghdl(with_tb=False):
    print("📦 Analizando archivos VHDL con GHDL:")

    # 1. Siempre modules primero
    if Path("modules").exists():
        if not analizar_archivos("modules", "módulos"):
            return
    else:
        print("⚠️  La carpeta 'modules/' no existe.")

    # 2. Luego src
    if Path("src").exists():
        if not analizar_archivos("src", "top-level"):
            return
    else:
        print("⚠️  La carpeta 'src/' no existe.")

    # 3. Solo si se pide --with-tb
    if with_tb:
        if Path("tb").exists():
            if not analizar_archivos("tb", "testbenches"):
                return
        else:
            print("⚠️  La carpeta 'tb/' no existe.")

    print("✅ Análisis completo con GHDL 🎉")
