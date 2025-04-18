# src/puerro/utils/config.py

from configparser import ConfigParser


def obtener_top_module():
    config = ConfigParser()
    config.read("apio.ini")

    try:
        return config["env"]["top-module"]
    except KeyError:
        print("❌ No se encontró 'top-module' en [env] de apio.ini")
        return None
