# Puerro CLI

**`puerro`** es una herramienta de línea de comandos que extiende **APIO** para facilitar el flujo de trabajo con código VHDL:

- **Inicialización** de proyectos APIO + VHDL
- **Generación** de archivos VHDL básicos
- **Análisis** con GHDL
- **Simulación** y visualización con GTKWave
- **Conversión** a Verilog con Yosys + GHDL
- **Síntesis** y **carga** en FPGA con APIO

---

## 📦 Instalación

Requisitos:

- Python 3.7+
- APIO instalado y en tu `PATH`
- GHDL, Yosys, GTKWave en tu `PATH`

Desde la raíz del proyecto:

```bash
pip install -e .
```

Esto crea el comando global `puerro`.

Enlaces de instalación de herramientas:

- [APIO](https://github.com/FPGAwars/apio)
- [GHDL](https://github.com/ghdl/ghdl)
- [Yosys](https://github.com/YosysHQ/yosys)
- [GTKWave](https://github.com/gtkwave/gtkwave)
- [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin)

---

## ⚙️ Comandos disponibles

### 1. `puerro init`

Inicializa un proyecto APIO + VHDL:

```bash
puerro init -b <board-name>
```

- Ejecuta `apio init -b <board-name>`
- Genera carpeta `src/` con `main.vhdl` base
- Genera subcarpetas: `src/tb/`, `src/build/`, `src/wave/`
- Copia `apio.ini` a `src/build/`

---

### 2. `puerro add`

Crea un nuevo módulo VHDL en `src/`:

```bash
puerro add <module-name>
```

Genera `src/<module-name>.vhdl` con plantilla de entidad y arquitectura.

---

### 3. `puerro ghdl`

Analiza módulos y top-level con GHDL:

```bash
puerro ghdl [--with-tb]
```

- Analiza `modules/*.vhdl` y `src/*.vhdl`.
- Con `--with-tb`, también analiza `tb/*.vhdl`.

---

### 4. `puerro sim`

Simula el testbench definido en `apio.ini` (`top-module`) y abre GTKWave:

```bash
puerro sim
```

- Elabora con `ghdl -e <top-module>`
- Ejecuta con `ghdl -r <top-module> --vcd=src/wave/<top-module>.vcd`
- Abre GTKWave sobre ese `.vcd`

---

### 5. `puerro verilog`

Convierte el `top-module` VHDL a Verilog en `src/build/`:

```bash
puerro verilog
```

- Usa Yosys + GHDL para generar `src/build/<top-module>.v`

---

### 6. `puerro build`

Sinte**t**iza y genera bitstream con APIO, colocando TODO en `src/build/`:

```bash
puerro build
```

- Ejecuta internamente `puerro verilog`.
- Copia `apio.ini` a `src/build/`.
- Lanza `apio build` desde `src/build/`.
- Deja artefactos (`.bin`, `.asc`, etc.) en `src/build/`.

---

### 7. `puerro upload`

Carga el bitstream a la FPGA:

```bash
puerro upload
```

- Ejecuta `apio upload` desde `src/build/`.

---

## 📂 Estructura del proyecto

```
.
├── apio.ini
├── pyproject.toml
├── src/
│   ├── main.py          # Entrada CLI (desarrollo)
│   └── puerro/
│       ├── cli.py
│       ├── commands/
│       │   ├── puerro_add.py
│       │   ├── puerro_ghdl.py
│       │   ├── puerro_init.py
│       │   ├── puerro_sim.py
│       │   ├── puerro_verilog.py
│       │   ├── puerro_build.py
│       │   └── puerro_upload.py
│       └── utils/
│           ├── config.py
│           └── filesystem.py
```

---
