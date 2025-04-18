import os
import re
from pathlib import Path

PLANTILLA_VHDL = """\
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity {nombre} is
    -- Puertos aquí
end {nombre};

architecture rtl of {nombre} is
    -- Señales internas aquí
begin
    -- Lógica aquí
end rtl;
"""


def run_add(nombre):
    if not nombre:
        print("❌ Error: El nombre del módulo no puede estar vacío")
        return

    # Validar que el nombre sea un identificador VHDL válido
    if not re.match(r"^[a-zA-Z][a-zA-Z0-9_]*$", nombre):
        print(
            "❌ Error: El nombre del módulo debe comenzar con una letra y solo puede contener letras, números y guiones bajos"
        )
        return

    os.makedirs("src/module", exist_ok=True)
    ruta_archivo = Path("src/module") / f"{nombre}.vhdl"

    if ruta_archivo.exists():
        print(f"❌ Error: El módulo '{nombre}' ya existe en '{ruta_archivo}'")
        return

    try:
        with open(ruta_archivo, "w") as f:
            f.write(PLANTILLA_VHDL.format(nombre=nombre))
        print(f"✅ Módulo '{nombre}' creado exitosamente en '{ruta_archivo}'")
    except Exception as e:
        print(f"❌ Error al crear el módulo: {str(e)}")
