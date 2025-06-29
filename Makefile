
# Makefile for the account_credential_editor project

# Define the virtual environment's python and pip executables
VENV_PYTHON := .venv/bin/python
VENV_PIP := .venv/bin/pip

.PHONY: install run clean help

help:
	@echo "Makefile for the account_credential_editor project"
	@echo ""
	@echo "Targets:"
	@echo "  install    - Install dependencies from requirements.txt"
	@echo "  run        - Run the main application"
	@echo "  clean      - Remove __pycache__ directories and .pyc files"

install:
	@echo "Installing dependencies..."
	$(VENV_PIP) install -r requirements.txt

run:
	@echo "Running the application..."
	$(VENV_PYTHON) main.py

clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} +
