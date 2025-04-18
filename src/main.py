# src/main.py

import argparse
import subprocess


def run_apio_init(board):
    cmd = ["apio", "init"]
    if board:
        cmd += ["-b", board]
    subprocess.run(cmd, check=True)


def main():
    parser = argparse.ArgumentParser(
        description="Puerro - CLI para proyectos VHDL con APIO"
    )
    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser("init", help="Inicializa un proyecto con APIO")
    init_parser.add_argument(
        "-b", "--board", help="Placa a utilizar (como en apio init -b ...)"
    )

    args = parser.parse_args()

    if args.command == "init":
        run_apio_init(args.board)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
