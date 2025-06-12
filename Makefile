.PHONY: all install install-uv install-python install-tools help

# Default target
all: install

# Complete installation
install: install-uv install-python install-tools
	@echo ""
	@echo "✅ Installation complete!"
	@echo ""
	@echo "After installation, activate the environment with:"
	@echo "  source .venv/bin/activate"
	@echo ""
	@echo "Then set the required environment variables:"
	@printf "  export PYBINDPLUGIN=\$$(python -c \"import pyangbind; import os; print(os.path.dirname(pyangbind.__file__) + '/plugin')\")\n"
	@echo '  export PYTHONWARNINGS="ignore::UserWarning:pyang.plugin"'

# Install uv
install-uv:
	@echo "📦 Installing uv..."
	@if ! command -v uv >/dev/null 2>&1; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		echo "✓ uv installed"; \
		echo ""; \
		echo "Add uv to your PATH by running:"; \
		echo "  source $$HOME/.cargo/env"; \
		echo "Or add this to your shell profile"; \
	else \
		echo "✓ uv is already installed"; \
	fi

# Install Python packages using uv
install-python:
	@echo "🐍 Setting up Python environment with uv..."
	@if [ ! -d ".venv" ]; then \
		uv venv .venv && \
		echo "✓ Virtual environment created"; \
		echo "📦 Installing Python packages into .venv..." && \
		VIRTUAL_ENV=$(pwd)/.venv uv pip install -r .devcontainer/requirements.txt && \
		echo "✓ Python packages installed"; \
	else \
		echo "✓ Virtual environment already exists - skipping Python package installation"; \
	fi

# Install external tools (gnmic, gnoic)
install-tools:
	@echo "🔧 Installing external tools..."
	@echo "Installing gnmic..."
	@bash -c "$$(curl -sL https://get-gnmic.openconfig.net)"
	@echo "Installing gnoic..."
	@bash -c "$$(curl -sL https://get-gnoic.kmrd.dev)"
	@echo "✓ External tools installed"

# Help
help:
	@echo "OpenConfig Lab Setup"
	@echo ""
	@echo "!!!! This is for labs not using devcontainer & containerlab !!!!"
	@echo ""
	@echo ""
	@echo "Usage:"
	@echo "  make                - Install everything (uv, Python packages, tools)"
	@echo "  make install        - Same as above"
	@echo "  make install-uv     - Install uv package manager only"
	@echo "  make install-python - Setup Python environment and packages"
	@echo "  make install-tools  - Install gnmic and gnoic only"
	@echo "  make help           - Show this help message"
	@echo ""
	@echo "After installation, activate the environment with:"
	@echo "  source .venv/bin/activate"
	@echo ""
	@echo "Then set the required environment variables:"
	@printf "  export PYBINDPLUGIN=\$$(python -c \"import pyangbind; import os; print(os.path.dirname(pyangbind.__file__) + '/plugin')\")\n"
	@echo '  export PYTHONWARNINGS="ignore::UserWarning:pyang.plugin"'