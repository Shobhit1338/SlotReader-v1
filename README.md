# SlotReader-v1

Adaptive reading web app that helps schedule daily reading slots, generate verified AI summaries, and improve comprehension through feedback.  
Built with Next.js and Django for a fast, minimal reading workflow.

---

## setup

```bash
make install     # install all dependencies
make dev         # run frontend and backend together
```

or run separately:

```bash
make dev-frontend
make dev-backend
```

Environment templates are available in `.env.example` under each service.

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
Django · DRF · PostgreSQL · PgVector
Celery · Redis · GitHub Actions

---

## notes

* `make help` shows available commands
* detailed roadmap in `mvp_v_1_roadmap.md`
* CI/CD runs on push: lint, test, build
* deploys via Vercel (frontend) and Render (backend)

---

## purpose

Adaptive reading platform focused on structured learning, verified summaries, and efficient daily engagement.
