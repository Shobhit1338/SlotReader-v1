# SlotReader-v1

SlotReader-v1 — an adaptive reading web app that helps you schedule daily reading slots, get AI-powered summaries, and improve through feedback. Built with Next.js and Django, it's a fast 20-day MVP showing how personalized reading can fit into any routine.

## Setup

### Backend (Django)

1. Activate the virtual environment:

   ```bash
   source venv/bin/activate
   ```

2. Install dependencies (if not already installed):

   ```bash
   pip install -r backend/requirements.txt
   ```

3. Set up environment variables in `backend/.env` (see `backend/core/settings.py` for required variables)

4. Run Django development server:

   ```bash
   cd backend
   python manage.py runserver
   ```

### Frontend (Next.js)

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies (if not already installed):

   ```bash
   npm install
   ```

3. Run the development server:

   ```bash
   npm run dev
   ```
