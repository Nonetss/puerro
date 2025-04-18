# src/puerro/utils/filesystem.py

import os


def crear_estructura_directorios():
    # Creamos el documento main.vhdl
    os.makedirs("src", exist_ok=True)
    with open("src/main.vhdl", "w") as f:
        f.write(
            f"""\
library IEEE;
use IEEE.STD_LOGIC_1164.all;
use IEEE.NUMERIC_STD.all;
entity main is

end entity main;
"""
        )

    with open("pins.pcf", "w") as f:
        f.write(
            """\
# Pins de ejemplo para la placa
# Cambia esto por los pines reales de tu placa
set_io contador[0]  45
set_io contador[1]  44
set_io contador[2]  43
set_io contador[3]  42
set_io contador[4]  41
set_io contador[5]  39
set_io contador[6]  38
set_io contador[7]  37

set_io clk 49


set_io start 33
"""
        )

    for carpeta in ["tb", "build", "wave"]:
        os.makedirs(f"src/{carpeta}", exist_ok=True)
        print(f"📁 Carpeta '{carpeta}/' creada.")
