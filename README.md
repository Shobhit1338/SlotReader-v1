# SlotReader-v1

SlotReader-v1 — an adaptive reading web app that helps you schedule daily reading slots, get AI-powered summaries, and improve through feedback. Built with Next.js and Django, it's a fast 20-day MVP showing how personalized reading can fit into any routine.

## Quick Start

### Install All Dependencies

```bash
# Using Make (recommended)
make install

# Or manually:
# Backend
source venv/bin/activate
pip install -r backend/requirements.txt

# Frontend
cd frontend && npm install
```

### Run Development Servers

```bash
# Run both frontend and backend (recommended)
make dev

# Or run individually:
make dev-frontend    # Frontend only
make dev-backend     # Backend only

# Or using npm from root:
npm run dev          # Frontend
```

## Setup

### Backend (Django)

1. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   # Or use: make venv
   ```

2. Install dependencies (if not already installed):

   ```bash
   make install-backend
   # Or: pip install -r backend/requirements.txt
   ```

3. Set up environment variables in `backend/.env` (see `backend/core/settings.py` for required variables)

4. Run Django development server:

   ```bash
   make dev-backend
   # Or: cd backend && python manage.py runserver
   ```

### Frontend (Next.js)

#### From Root Directory (Recommended)

All npm commands can be run from the root directory:

```bash
# Install dependencies
npm run frontend:install
# Or: make install-frontend

# Development server
npm run dev
# Or: make dev-frontend

# Build for production
npm run build

# Linting and formatting
npm run lint              # Run ESLint
npm run format            # Format code with Prettier
npm run format:check      # Check code formatting
npm run type-check        # TypeScript type checking
```

#### From Frontend Directory

Alternatively, you can work directly in the `frontend/` directory:

```bash
cd frontend
npm install
npm run dev
```

## Available Commands

### Using Make (Recommended)

Run `make help` to see all available commands:

```bash
make help              # Show all available commands
make install           # Install all dependencies
make dev               # Run both frontend and backend
make build             # Build frontend for production
make lint              # Lint frontend code
make format            # Format frontend code
make format-check      # Check formatting
make type-check        # Type check frontend
make clean             # Clean all build artifacts
```

### Using NPM from Root

```bash
npm run dev            # Run frontend dev server
npm run build          # Build frontend
npm run start          # Start production server
npm run lint           # Lint code
npm run format         # Format code
npm run format:check   # Check formatting
npm run type-check     # Type check
```

## CI/CD

The project includes GitHub Actions workflows for automated CI/CD:

- **Frontend CI/CD** (`.github/workflows/frontend.yml`):
  - Runs on push/PR to `main` or `develop` branches
  - Executes: lint, format-check, type-check, and build
  - Uses Node.js 20 and npm caching for optimal performance

The CI pipeline ensures code quality and prevents broken builds from being merged.

## Project Structure

```
SlotReader-v1/
├── frontend/          # Next.js frontend application
├── backend/           # Django backend API
├── venv/              # Python virtual environment
├── package.json       # Root npm scripts (proxies to frontend)
├── Makefile           # Convenient make commands
└── .github/           # GitHub Actions workflows
```
