import subprocess
from pathlib import Path

from puerro.utils.config import obtener_top_module


def run_verilog():
    top = obtener_top_module()
    if not top:
        return

    src_dir = Path("src")
    mod_dir = src_dir / "module"
    src_file = src_dir / f"{top}.vhdl"
    out_file = src_dir / "build" / f"{top}.v"

    if not src_file.exists():
        print(f"❌ No se encontró el archivo VHDL: {src_file}")
        return

    print(f"🔄 Generando Verilog desde '{src_file}'...")

    # Recolectar todos los archivos VHDL (módulos + top-level)
    vhdl_files = []
    if mod_dir.exists():
        vhdl_files += sorted(mod_dir.glob("*.vhdl"))
    vhdl_files.append(src_file)

    # Construir script para Yosys con plugin GHDL
    # Usamos un solo comando GHDL que compila todos los VHDL y elabora el top
    files_list = " ".join(str(f) for f in vhdl_files)
    yosys_script = f"ghdl {files_list} -e {top}; write_verilog {out_file}"

    cmd = ["yosys", "-m", "ghdl", "-p", yosys_script]

    try:
        subprocess.run(cmd, check=True)
        print(f"✅ Verilog generado en '{out_file}'")
    except subprocess.CalledProcessError:
        print("❌ Error al ejecutar Yosys para conversión a Verilog.")
