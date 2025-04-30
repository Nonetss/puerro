import shutil
import subprocess


def run_make():
    try:
        print("🔧 Ejecutando 'make'...")
        subprocess.run(["puerro", "ghdl"], check=True)
        subprocess.run(["puerro", "verilog"], check=True)
        subprocess.run(["puerro", "build"], check=True)
        subprocess.run(["puerro", "upload"], check=True)

    except subprocess.CalledProcessError as e:
        print(f"❌ Error durante el proceso de construcción: {e}")
        return
