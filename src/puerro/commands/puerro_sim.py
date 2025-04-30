import subprocess
import time
from pathlib import Path

from puerro.utils.config import obtener_top_module


def run_sim(entity_name=None, use_wave=False):
    # 1. Detectar testbench único
    if entity_name is None:
        tb_dir = Path("src/tb")
        tbs = list(tb_dir.glob("*.vhdl"))
        if len(tbs) == 1:
            entity_name = tbs[0].stem
            print(f"ℹ️  Detectado testbench único: '{entity_name}'")
        else:
            entity_name = obtener_top_module()
    entidad = entity_name or ""
    if not entidad:
        print("❌ No hay entidad para simular.")
        return

    # 2. Preparar workdir
    workdir = Path("src/build")
    workdir.mkdir(parents=True, exist_ok=True)

    # 3. Analizar VHDL
    print("🔍 Analizando archivos VHDL...")
    for f in sorted(Path("src").rglob("*.vhdl")):
        print(f"  → {f}")
        try:
            subprocess.run(["ghdl", "-a", f"--workdir={workdir}", str(f)], check=True)
        except subprocess.CalledProcessError:
            print(f"❌ Error al analizar {f}")
            return

    # 4. Preparar salida
    ext = "ghw" if use_wave else "vcd"
    wave_dir = Path("src/wave")
    wave_dir.mkdir(exist_ok=True)
    wave_path = wave_dir / f"{entidad}.{ext}"
    if wave_path.exists():
        wave_path.unlink()

    # 5. Elaborar
    print(f"🔧 Elaborando entidad '{entidad}'...")
    try:
        subprocess.run(["ghdl", "-e", f"--workdir={workdir}", entidad], check=True)
    except subprocess.CalledProcessError:
        print("❌ Error al elaborar con GHDL")
        return

    # 6. Simular (no abortar si hay assertion-failure)
    print(f"▶️ Ejecutando simulación y generando {ext.upper()} en '{wave_path}'...")
    start_time = time.time()
    result = subprocess.run(
        [
            "ghdl",
            "-r",
            f"--workdir={workdir}",
            entidad,
            f"--{ext}={wave_path}",
            "--stop-time=1ms",
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    sim_time = time.time() - start_time

    # Si GHDL devolvió error, pero el archivo existe, lo ignoramos
    if result.returncode != 0:
        print("⚠️ Simulación terminó con errores (assertion), revisa mensaje:")
        print(result.stderr.strip())

    if not wave_path.exists():
        print(f"❌ Archivo {ext.upper()} no generado.")
        return

    print(f"📈 Simulación completada en {sim_time:.2f}s")

    # 7. Pausa antes de abrir GTKWave
    pause_secs = 2
    print(f"⏳ Esperando {pause_secs}s antes de abrir GTKWave...")
    time.sleep(pause_secs)

    # 8. Abrir GTKWave
    print("📊 Abriendo GTKWave...")
    try:
        subprocess.run(["gtkwave", str(wave_path)])
    except FileNotFoundError:
        print("❌ GTKWave no está instalado o no se encuentra en el PATH.")
