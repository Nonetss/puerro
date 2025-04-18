# src/puerro/cli.py

import argparse

from puerro.commands.puerro_init import run_init


def main():
    parser = argparse.ArgumentParser(
        prog="puerro", description="CLI para proyectos VHDL con APIO"
    )
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Inicializa un proyecto con APIO")
    init_parser.add_argument("-b", "--board", help="Placa a utilizar")

    args = parser.parse_args()

    if args.command == "init":
        run_init(board=args.board)
    else:
        parser.print_help()
