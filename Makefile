# Define variables
PROJECT_NAME = excel_to_pdf
VENV_DIR = venv
REQUIREMENTS_FILE = requirements.txt
GITHUB_REPO = https://github.com/Lusija777/excel_to_pdf.git

# Default target
all: setup

setup: install_python clone_repo venv

# Install Python 3 and pip
install_python:
	@echo "Installing Python 3..."
	sudo apt-get update
	sudo apt-get install -y python3 python3-venv python3-pip
	@echo "Python 3 installed."

# Clone the project from GitHub
clone_repo:
	@if [ ! -d "$(PROJECT_NAME)" ]; then \
		echo "Cloning the project from GitHub..."; \
		git clone $(GITHUB_REPO) $(PROJECT_NAME); \
		echo "Repository cloned."; \
	else \
		echo "Project already cloned, skipping..."; \
	fi

# Create a virtual environment and install dependencies
venv:
	@echo "Creating virtual environment..."
	cd $(PROJECT_NAME) && python3 -m venv $(VENV_DIR)
	@echo "Virtual environment created."
	@echo "Installing dependencies..."
	cd $(PROJECT_NAME) && $(VENV_DIR)/bin/pip install -r $(REQUIREMENTS_FILE)
	@echo "Dependencies installed."

# Freeze the current environment's packages to a requirements file
requirements:
	@echo "Generating requirements.txt..."
	cd $(PROJECT_NAME) && $(VENV_DIR)/bin/pip freeze > $(REQUIREMENTS_FILE)
	@echo "requirements.txt generated."

# Run the project
run:
	@echo "Running the project..."
	cd $(PROJECT_NAME) && $(VENV_DIR)/bin/python create_pdf.py

.PHONY: all install_python clone_repo init venv requirements run
