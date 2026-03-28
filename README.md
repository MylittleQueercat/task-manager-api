# Task Manager API

![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Render](https://img.shields.io/badge/Deployed-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)

A RESTful API for task management, built with FastAPI and PostgreSQL.  
**🌐 Live demo**: https://task-manager-api-e8k0.onrender.com/docs

---

## ✨ Features

- ✅ Full CRUD for tasks (GET / POST / PUT / DELETE)
- ✅ PostgreSQL database with SQLAlchemy ORM
- ✅ JWT authentication (register / login / protected routes)
- ✅ Per-user data isolation (users only see their own tasks)
- ✅ Pydantic validation on all inputs
- ✅ pytest test suite
- ✅ Docker + docker-compose
- ✅ Deployed on Render.com + Supabase

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Language | Python 3.11 |
| Database | PostgreSQL (Supabase) |
| ORM | SQLAlchemy 2.0 |
| Auth | JWT (python-jose + passlib/bcrypt) |
| Validation | Pydantic v2 |
| Testing | pytest |
| Containerization | Docker + docker-compose |
| Deployment | Render.com |

---

## 📁 Project Structure

```
task-manager-api/
├── main.py          # Routes and app entry point
├── models.py        # SQLAlchemy models (User, Task)
├── schemas.py       # Pydantic schemas (request/response validation)
├── auth.py          # JWT logic (create/decode token, hash password)
├── database.py      # DB connection and session management
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```

---

## 🔌 API Endpoints

### 🔐 Auth
| Method | Endpoint | Description | Auth required |
|---|---|---|---|
| POST | /register | Create a new user | ❌ |
| POST | /login | Get JWT token | ❌ |

### 📋 Tasks
| Method | Endpoint | Description | Auth required |
|---|---|---|---|
| GET | /tasks | Get all tasks for current user | ✅ |
| GET | /tasks/{id} | Get a specific task | ✅ |
| POST | /tasks | Create a new task | ✅ |
| PUT | /tasks/{id} | Update a task | ✅ |
| DELETE | /tasks/{id} | Delete a task | ✅ |

---

## 🚀 Run Locally

### Option 1 — Docker (recommended)

```bash
git clone https://github.com/MylittleQueerCat/task-manager-api.git
cd task-manager-api
docker-compose up --build
```

API available at: http://localhost:8000/docs

### Option 2 — Virtual environment

```bash
git clone https://github.com/MylittleQueerCat/task-manager-api.git
cd task-manager-api

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:
```
DB_URL=postgresql://localhost/taskmanager
SECRET_KEY=your_secret_key
```

```bash
uvicorn main:app --reload
```

API available at: http://localhost:8000/docs

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `DB_URL` | PostgreSQL connection URL |
| `SECRET_KEY` | Secret key for signing JWT tokens |

---

## 🔒 Authentication Flow

```
POST /register  →  create user (password hashed with bcrypt)
POST /login     →  returns JWT access token (30min expiry)

# All /tasks routes require:
Authorization: Bearer <token>
```

---

## 🧪 Run Tests

```bash
pytest
```

---

## ☁️ Infrastructure Decisions

### Why Render.com for hosting?

Originally attempted deployment on **Railway**, but encountered an environment variable injection bug on their platform (not a code issue). Switched to Render, which offers a simpler deployment experience for Python APIs: auto-detects the runtime, reads `requirements.txt`, and redeploys automatically on every `git push`.

| | Render (free tier) | Railway (free tier) |
|---|---|---|
| Python support | ✅ Native | ✅ Native |
| Auto-deploy on push | ✅ | ✅ |
| PostgreSQL included | ✅ (90-day limit) | ✅ |
| Reliability | ✅ Stable | ⚠️ Env var bugs |
| Cold start | ⚠️ ~30s after 15min idle | ⚠️ Similar |
| Custom domains | ✅ | ✅ |

**Limitation**: Free tier sleeps after 15 minutes of inactivity. First request after idle takes ~10–30 seconds to respond (cold start).

---

### Why Supabase for the database?

Render's free PostgreSQL is deleted after **90 days**. For a project meant to store real data long-term, Supabase is a better choice: free tier with persistent storage, a built-in web UI to inspect the database, and standard PostgreSQL — no code changes needed, just swap the `DB_URL`.

| | Supabase (free tier) | Render PostgreSQL (free tier) |
|---|---|---|
| Data persistence | ✅ Permanent | ⚠️ Deleted after 90 days |
| Web UI | ✅ Built-in table editor | ❌ |
| Standard PostgreSQL | ✅ | ✅ |
| IPv4 support | ✅ Via connection pooler | ✅ |
| Region (EU) | ✅ | ✅ |

**Note**: Render's free tier only supports IPv4. Supabase's direct connection uses IPv6, which causes a `Network is unreachable` error. Solution: use Supabase's **Session Pooler** URL (`pooler.supabase.com`) instead of the direct URL (`db.supabase.co`).

---

## 📚 Key Concepts Implemented

**🗄️ ORM (Object-Relational Mapping)**  
SQLAlchemy maps Python classes to database tables. Instead of writing raw SQL, you interact with Python objects — similar to writing a C struct and having the persistence handled automatically.

**🎫 JWT (JSON Web Token)**  
Stateless authentication: the server signs a token with a secret key and sends it to the client. On each request, the server verifies the signature — no session stored server-side. Think of it like a signed certificate: anyone can read it, but only the server can produce a valid one.

**💉 Dependency Injection**  
FastAPI's `Depends()` system automatically resolves and injects dependencies (DB session, current user) into route functions. Equivalent to passing a context/config struct through a call chain in C, but handled by the framework.

**✅ Pydantic Validation**  
All incoming request bodies are validated against a schema before hitting your route logic. Wrong type or missing field = automatic 422 response, no manual checks needed.

**🐳 Docker**  
Packages the app and its environment into an isolated container — guarantees it runs the same everywhere, regardless of the host system.
