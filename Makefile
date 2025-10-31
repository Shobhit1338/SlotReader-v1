.PHONY: help install-frontend install-backend install dev-frontend dev-backend dev build lint format format-check type-check clean-frontend clean-backend clean test-frontend venv activate

# Default target
help:
	@echo "SlotReader-v1 Makefile Commands:"
	@echo ""
	@echo "Setup:"
	@echo "  make venv              - Activate virtual environment"
	@echo "  make install-frontend  - Install frontend dependencies"
	@echo "  make install-backend   - Install backend dependencies"
	@echo "  make install           - Install all dependencies"
	@echo ""
	@echo "Development:"
	@echo "  make dev-frontend      - Run frontend dev server"
	@echo "  make dev-backend       - Run backend dev server"
	@echo "  make dev               - Run both frontend and backend (parallel)"
	@echo ""
	@echo "Frontend:"
	@echo "  make build             - Build frontend for production"
	@echo "  make lint              - Lint frontend code"
	@echo "  make format            - Format frontend code"
	@echo "  make format-check      - Check frontend code formatting"
	@echo "  make type-check        - Type check frontend code"
	@echo "  make test-frontend     - Run frontend tests (if available)"
	@echo ""
	@echo "Cleanup:"
	@echo "  make clean-frontend    - Clean frontend build artifacts"
	@echo "  make clean-backend     - Clean backend artifacts"
	@echo "  make clean             - Clean all artifacts"

# Virtual environment activation (informational)
venv:
	@echo "To activate the virtual environment, run:"
	@echo "  source venv/bin/activate"
	@echo ""
	@echo "Or use: make activate"

activate:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		. venv/bin/activate; \
		echo "Virtual environment activated. Run commands in this shell session."; \
	else \
		echo "Virtual environment is already active: $$VIRTUAL_ENV"; \
	fi

# Installation
install-frontend:
	cd frontend && npm install

install-backend: venv
	. venv/bin/activate && pip install -r backend/requirements.txt

install: install-frontend install-backend
	@echo "All dependencies installed!"

# Development servers
dev-frontend:
	cd frontend && npm run dev

dev-backend: venv
	. venv/bin/activate && cd backend && python manage.py runserver

dev:
	@echo "Starting frontend and backend servers..."
	@echo "Press Ctrl+C to stop both servers"
	@make -j2 dev-frontend dev-backend

# Frontend commands
build:
	cd frontend && npm run build

lint:
	cd frontend && npm run lint

format:
	cd frontend && npm run format

format-check:
	cd frontend && npm run format:check

type-check:
	cd frontend && npm run type-check

test-frontend:
	@echo "No tests configured yet. Add test scripts to frontend/package.json"

# Cleanup
clean-frontend:
	cd frontend && rm -rf .next out node_modules/.cache *.tsbuildinfo

clean-backend:
	find backend -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find backend -type f -name "*.pyc" -delete
	find backend -type f -name "*.pyo" -delete
	find backend -type d -name "*.egg-info" -exec rm -r {} + 2>/dev/null || true

clean: clean-frontend clean-backend
	@echo "Cleanup complete!"

