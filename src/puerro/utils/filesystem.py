# src/puerro/utils/filesystem.py

import os


def crear_estructura_directorios():
    for carpeta in ["src", "tb", "build", "wave"]:
        os.makedirs(carpeta, exist_ok=True)
        print(f"📁 Carpeta '{carpeta}/' creada.")


def crear_makefile():
    contenido = """\
TOP=top

analyze:
\tghdl -a src/$(TOP).vhdl

elaborate:
\tghdl -e $(TOP)

run:
\tghdl -r $(TOP) --vcd=wave/$(TOP).vcd

build:
\tyosys -m ghdl -p "ghdl src/$(TOP).vhdl -e $(TOP); write_verilog build/$(TOP).v"

upload:
\tapio upload

clean:
\trm -f *.cf wave/*.vcd build/*.v
"""
    with open("Makefile", "w") as f:
        f.write(contenido)
    print("📝 Makefile creado.")
