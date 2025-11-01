# SlotReader-v1

Adaptive reading web app that helps schedule daily reading slots, generate verified AI summaries, and improve comprehension through feedback.  
Built with Next.js and Django for a fast, minimal reading workflow.

---

## setup

```bash
# 1. Install dependencies
make install

# 2. Configure .env file
# Copy backend/.env.example to backend/.env
# Update DATABASE_URL with your Supabase password

# 3. Run migrations
make migrate-db

# 4. Start development servers
make dev
```

---

## structure

```text
SlotReader-v1/
├── frontend/   # Next.js app
├── backend/    # Django API
├── Makefile
├── venv/
└── .github/
```

---

## stack

Next.js · Tailwind · TypeScript
Django · DRF · Supabase (PostgreSQL + PgVector)
Celery · Redis · GitHub Actions

---

## notes

* `make help` shows all available commands
* Run migrations: `make migrate-db`
* Configure `DATABASE_URL` in `backend/.env`
* Detailed roadmap in `SlotReader-MVP.md`

---

## purpose

Adaptive reading platform focused on structured learning, verified summaries, and efficient daily engagement.
