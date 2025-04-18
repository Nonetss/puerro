# src/puerro/cli.py

from puerro.commands.puerro_add import run_add
from puerro.commands.puerro_build import run_build
from puerro.commands.puerro_ghdl import run_ghdl
from puerro.commands.puerro_init import run_init
from puerro.commands.puerro_sim import run_sim
from puerro.commands.puerro_upload import run_upload
from puerro.commands.puerro_verilog import run_verilog


def main():
    import argparse

    parser = argparse.ArgumentParser(
        prog="puerro", description="CLI para proyectos VHDL con APIO"
    )
    subparsers = parser.add_subparsers(dest="command")

    # init
    parser_init = subparsers.add_parser("init", help="Inicializa un proyecto con APIO")
    parser_init.add_argument("-b", "--board", help="Placa a utilizar")

    # add
    parser_add = subparsers.add_parser("add", help="Crea un nuevo módulo VHDL")
    parser_add.add_argument("nombre", help="Nombre del nuevo módulo")

    # ghdl
    parser_ghdl = subparsers.add_parser(
        "ghdl", help="Analiza los archivos VHDL en src/ con GHDL"
    )
    parser_ghdl.add_argument(
        "--with-tb",
        action="store_true",
        help="También analiza los testbenches en la carpeta 'tb/'",
    )

    # sim
    parser_sim = subparsers.add_parser(
        "sim", help="Simula la entidad indicada en apio.ini"
    )

    # verilog
    parser_verilog = subparsers.add_parser(
        "verilog", help="Convierte el VHDL a Verilog usando Yosys"
    )

    # build
    parser_build = subparsers.add_parser(
        "build", help="Compila el proyecto usando APIO"
    )

    # upload
    parser_upload = subparsers.add_parser(
        "upload", help="Sube el diseño a la FPGA usando APIO"
    )

    args = parser.parse_args()

    if args.command == "init":
        run_init(board=args.board)
    elif args.command == "add":
        run_add(nombre=args.nombre)
    elif args.command == "ghdl":
        run_ghdl(with_tb=args.with_tb)
    elif args.command == "sim":
        run_sim()
    elif args.command == "verilog":
        run_verilog()
    elif args.command == "build":
        run_build()
    elif args.command == "upload":
        run_upload()
    else:
        parser.print_help()
