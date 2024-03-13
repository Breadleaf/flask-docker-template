PYTHON = python3
PIP = pip

MAIN = client.py

PORT = 3000
HOST = 0.0.0.0

help:
	@echo "help: show this help"
	@echo "setup: setup the client"
	@echo "start: start the client"
	@echo "start-no-setup: start the client without setting up"
	@echo "clean: clean the files not needed"

setup:
	@echo "Setting up the client"
	@$(PYTHON) -m venv venv \
		&& venv/bin/$(PIP) install --upgrade pip \
		&& venv/bin/$(PIP) install -r requirements.txt

start: setup
	@echo "Starting the client"
	@ if [ -f venv/bin/$(PYTHON) ]; then \
		venv/bin/$(PYTHON) $(MAIN) $(HOST) $(PORT); \
	else \
		echo "ERROR: The client is not set up"; \
		exit 1; \
	fi

start-no-setup:
	@echo "Starting the client"
	@ if [ -f venv/bin/$(PYTHON) ]; then \
		venv/bin/$(PYTHON) $(MAIN) $(HOST) $(PORT); \
	else \
		echo "ERROR: The client is not set up"; \
		exit 1; \
	fi

clean:
	@echo "Cleaning the files not needed"
	@rm -rf venv

.PHONY: help setup start start-no-setup clean
