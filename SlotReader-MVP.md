# 🚀 MVP V1 Development Roadmap  

### *Adaptive Reading Scheduler – 20-Day Web App Build Plan*  

---

## 🌐 Project Overview

This 20-day sprint delivers a production-ready **MVP web app** that proves the adaptive reading concept.  
Users can onboard, schedule reading slots, receive verified summaries (LLM + RAG), and read via a responsive Next.js interface.  
All core systems—content pipeline, scheduler, and verification—will be architected for later extension into mobile (iOS/Android) front-ends.

**Primary Goal:**  
> Build, test, and deploy a functional MVP on GitHub (Next.js + Django) within 20 days, enabling daily verified reading sessions.

---

## 🧱 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | Next.js 14 (App Router + Tailwind CSS + TypeScript) |
| **Backend** | Django + Django REST Framework |
| **Async Jobs** | Celery + Redis |
| **Database** | PostgreSQL + PgVector |
| **LLM / RAG** | OpenAI / Gemini API + FAISS/PgVector retrieval |
| **Hosting** | Render / Railway / Vercel (Frontend) |
| **CI/CD** | GitHub Actions |
| **Monitoring** | PostHog / Sentry (optional post-MVP) |

---

## 🗓️ Sprint Timeline (20 Days)

### **Phase 1 – Setup & Architecture ( Days 1–3 )**  

**Objective:** establish development foundation and automated CI/CD pipeline.

**Deliverables**

- GitHub repository created with folders:

  ```
  /frontend
  /backend
  /docs
  /infra
  ```

- Branch protection rules (`main`, `develop`) enabled.
- **Backend setup:**
  - Initialize Django project, add DRF.
  - Configure PostgreSQL connection and PgVector extension.
  - Basic models: User, Topic, Schedule, Summary.
  - Configure Celery + Redis for async tasks.
- **Frontend setup:**
  - Create Next.js project (TypeScript + Tailwind).
  - Add ESLint + Prettier config.
- **Infra & CI/CD:**
  - GitHub Actions for lint + test + build.
  - `.env.example` + `.env.local` templates.
  - Docker compose (optional for local dev).  

---

### **Phase 2 – Design System & UX Foundation ( Days 4–5 )**  

**Objective:** define visual language and core layouts for web experience.

**Deliverables**

- UI kit: colors, fonts, shadows, buttons, cards (Tailwind components).
- Create global layout and navigation (header / side menu / footer).
- Key pages mocked in Figma:
  - Onboarding Flow (3 steps)  
  - Today’s Read Page  
  - Weekly Schedule Page (progress overview)
- Mobile responsive designs for all.
- Component architecture in Next.js (`/components`, `/lib`, `/hooks`).  

---

### **Phase 3 – Onboarding & Personalization ( Days 6–8 )**  

**Objective:** collect user persona data and initialize first weekly plan.

**Deliverables**

- Frontend flow:
  - Step 1: Select persona (Techie / Business / Student / Freelancer).  
  - Step 2: Pick topics or add custom input (URL, keyword, PDF, YouTube).  
  - Step 3: Select goal (5 reads/week) and time slot (9 AM–10 AM).  
  - Confirmation screen → “Plan Ready”.
- Backend API (`/api/v1/onboard`) creates:
  - User record + preferences  
  - Topics + Schedule templates  
  - Initial placeholder items for Mon–Fri
- Integration test covering end-to-end flow.
- UI state management via React Context / Zustand.  

---

### **Phase 4 – Scheduler & Content Generation ( Days 9–12 )**  

**Objective:** implement core logic for reading plan generation and content creation.

**Deliverables**

- **Weekly Planner** (Celery Task): scores topics, fills Mon–Fri slots.
- **Daily Precompute Job:** runs 22:00 each night → fetches sources and generates summaries.
- **LLM + RAG Integration:**
  - chunking & embedding via PgVector.  
  - “Recap” and “Bullets” formats for MVP.  
  - Store citation spans and verification score.
- **Verification Layer:**
  - citation density check (≥ 1 per 120 words).  
  - numeric consistency validation.  
  - badge (GREEN/AMBER/RED).
- API routes:  
  - `GET /schedule/today` → returns ready summary.  
  - `POST /feedback` → stores rating & session data.
- Logging & task monitoring via Flower / Celery Dashboard.  

---

### **Phase 5 – Reader Experience ( Days 13–15 )**  

**Objective:** deliver main reading UI with format toggling and progress tracking.

**Deliverables**

- **Today’s Read Page:**
  - title + topic + verification badge  
  - summary content area with format switcher  
  - source citations hover tooltips
- **Progress Tracker:**
  - streak counter and completion meter.  
  - auto-mark done on scroll complete.  
- **Feedback Widget:** stars + comment tags (too long / short / etc.).
- Responsive cards for tablet/mobile web.
- Analytics events (logging completion + dwell time).  

---

### **Phase 6 – Feedback Loop & Adaptive Logic ( Days 16–17 )**  

**Objective:** feed user behavior into scheduler to refine content depth and topic mix.

**Deliverables**

- Backend logic for adaptive weights:
  - If “too long” → reduce token count 20%.  
  - If “irrelevant” → topic penalty 0.7.  
  - If “liked” → boost domain trust.  
- Update `WeeklyPlanner` to use feedback coefficients.
- Streak milestone notifications (“3 days in a row ✅”).  
- Aggregate feedback dashboard (`/admin/analytics`).  

---

### **Phase 7 – Testing & Quality Assurance ( Days 18–19 )**  

**Objective:** validate end-to-end stability and performance before release.

**Deliverables**

- **Backend tests:** pytest + factory_boy; coverage ≥ 80%.  
- **Frontend tests:** Jest + React Testing Library for core flows.  
- **Manual QA Checklist:**
  1. Onboarding → Plan → Read → Feedback.  
  2. LLM latency < 5 s (avg).  
  3. Scheduler tasks executing nightly.  
- **Bug triage:** label issues in GitHub Projects.  
- **Security:** CORS, API auth tokens, env secret audit.  

---

### **Phase 8 – Deployment & Handover ( Day 20 )**  

**Objective:** ship a live, testable MVP hosted entirely via GitHub.

**Deliverables**

- **Frontend Deploy:** Vercel connected to `main` branch.  
- **Backend Deploy:** Render / Railway auto-deploy from `main`.  
- **CI/CD Workflow:** on merge → build → migrate → deploy.  
- Create `CHANGELOG.md` and `README.md` with:
  - local setup steps  
  - .env variables  
  - deployment notes
- Open GitHub Issues for beta feedback.  
- Tag release: `v1.0.0-beta`.  

---

## 📊 Phase-wise Deliverable Summary

| Phase | Duration | Core Output |
|-------|-----------|-------------|
| 1. Setup & Architecture | 1 – 3 | Repo + infra + CI ready |
| 2. Design System | 4 – 5 | UI kit + layout structure |
| 3. Onboarding | 6 – 8 | Persona flow + API integration |
| 4. Scheduler Engine | 9 – 12 | Automated daily summaries |
| 5. Reader UI | 13 – 15 | Functional reading page |
| 6. Feedback Loop | 16 – 17 | Adaptive tuning engine |
| 7. Testing & QA | 18 – 19 | Stable build + 80 % coverage |
| 8. Deployment | 20 | Live GitHub-based MVP |

---

## 📦 Supporting Artifacts

- `/docs/architecture.md` – system diagram + ERD  
- `/docs/api_reference.md` – endpoints & schemas  
- `/docs/prompt_templates.md` – LLM prompt structure  
- `/docs/testing_checklist.md` – QA cases  
- `/docs/roadmap_v2.md` – post-MVP features (voice mode, flashcards, Notion export)

---

## 🚧 Post-MVP Next Steps (For v1.1 and Mobile)

1. Integrate voice summary mode (text-to-speech).  
2. Implement Notion / Readwise export.  
3. Add Team Spaces + shared reading lists.  
4. Build SwiftUI front-end reusing the same Django API.  
5. Add AI quiz / flashcard review engine.  

---

**End Goal:**  
> A clean, verified, habit-forming reading web app that adapts to each user’s learning style — production-ready backend, deployable via GitHub in 20 days.
