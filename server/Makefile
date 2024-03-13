PYTHON = python3
PIP = pip

MAIN = server.py

PORT = 5000
HOST = 0.0.0.0

help:
	@echo "help: show this help"
	@echo "setup: setup the server"
	@echo "start: start the server"
	@echo "start-no-setup: start the server without setting up"
	@echo "clean: clean the files not needed"

setup:
	@echo "Setting up the server"
	@$(PYTHON) -m venv venv \
		&& venv/bin/$(PIP) install --upgrade pip \
		&& venv/bin/$(PIP) install -r requirements.txt

start: setup
	@echo "Starting the server"
	@ if [ -f venv/bin/$(PYTHON) ]; then \
		venv/bin/$(PYTHON) $(MAIN) $(HOST) $(PORT); \
	else \
		echo "ERROR: The server is not set up"; \
		exit 1; \
	fi

start-no-setup:
	@echo "Starting the server"
	@ if [ -f venv/bin/$(PYTHON) ]; then \
		venv/bin/$(PYTHON) $(MAIN) $(HOST) $(PORT); \
	else \
		echo "ERROR: The server is not set up"; \
		exit 1; \
	fi

clean:
	@echo "Cleaning the files not needed"
	@rm -rf venv

.PHONY: help setup start start-no-setup clean
