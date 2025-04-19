# Makefile para instalar Yosys, GHDL, el plugin de GHDL para Yosys, y Apio
# Solo compatible con Debian y Ubuntu. Si no estás en una de esas distros... que te lo montes tú.

.PHONY: all check-distro install-deps install-yosys install-ghdl install-ghdl-plugin install-apio clean

# -------------------------
# TARGET PRINCIPAL
# -------------------------
all: check-distro install-deps install-yosys install-ghdl install-ghdl-plugin install-apio

# -------------------------
# CHEQUEO DE DISTRO
# -------------------------
check-distro:
	@. /etc/os-release; \
	if [ "$$ID" != "debian" ] && [ "$$ID" != "ubuntu" ]; then \
		echo "Este Makefile solo funciona en Debian o Ubuntu."; \
		exit 1; \
	else \
		echo "Distribución compatible: $$ID"; \
	fi

# -------------------------
# DEPENDENCIAS DEL SISTEMA
# -------------------------
install-deps:
	@echo "Instalando dependencias del sistema..."
	sudo apt update
	sudo apt install -y build-essential clang bison flex libreadline-dev gawk tcl-dev libffi-dev \
		git graphviz xdot pkg-config python3 libboost-system-dev libboost-python-dev \
		libboost-filesystem-dev zlib1g-dev gnat-10 libgnat-10 gcc g++ libieee1284-3-dev python3-venv
	@echo "Dependencias del sistema instaladas."

# -------------------------
# YOSYS
# -------------------------
install-yosys:
	@echo "Clonando e instalando Yosys..."
	@if [ ! -d yosys ]; then git clone https://github.com/YosysHQ/yosys; fi
	cd yosys && git submodule update --init --recursive && make -j$$(nproc)
	sudo make -C yosys install
	@echo "Yosys instalado."

# -------------------------
# GHDL
# -------------------------
install-ghdl:
	@echo "Clonando e instalando GHDL..."
	@if [ ! -d ghdl ]; then git clone https://github.com/ghdl/ghdl.git; fi
	cd ghdl && ./configure --prefix=/usr/local && make -j$$(nproc)
	sudo make -C ghdl install
	@echo "GHDL instalado."

# -------------------------
# PLUGIN GHDL PARA YOSYS
# -------------------------
install-ghdl-plugin:
	@echo "Instalando plugin GHDL para Yosys..."
	@if [ ! -d ghdl-yosys-plugin ]; then git clone https://github.com/ghdl/ghdl-yosys-plugin.git; fi
	cd ghdl-yosys-plugin && make -j$$(nproc)
	sudo make -C ghdl-yosys-plugin install
	@echo "Plugin GHDL para Yosys instalado."

# -------------------------
# APIO
# -------------------------
install-apio:
	@echo "Instalando Apio en entorno virtual..."
	python3 -m venv venv
	source venv/bin/activate && \
	pip install -U pip && \
	pip install -U apio packaging && \
	apio install --all && \
	apio drivers --ftdi-enable && \
	apio drivers --serial-enable
	@echo "Apio instalado. Para usarlo, activa el entorno virtual con 'source venv/bin/activate'."


# -------------------------
# PUERRO
# -------------------------

install-puerro:
	@echo "Instalando Puerro..."
	source venv/bin/activate && \
		pip install -e .
	@echo "Puerro instalado. Para usarlo, activa el entorno virtual con 'source venv/bin/activate'."

# -------------------------
# LIMPIEZA
# -------------------------
clean:
	rm -rf yosys ghdl ghdl-yosys-plugin venv-apio

