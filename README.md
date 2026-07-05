# Nano BNPL

A lightweight Django-based implementation of a Buy Now, Pay Later (BNPL) system.

## Overview

Nano BNPL is a minimal, efficient BNPL backend implemented with Django and Django Ninja (for fast APIs). The project focuses on clarity and quick setup so you can prototype BNPL flows, track transactions, and run automated tests.

## Features

- 💳 Core BNPL transaction models and management
- 🔄 Installment and payment scheduling support
- 📊 Transaction tracking and basic admin integration
- 🚀 REST API built with Django Ninja
- 🐳 Docker & docker-compose for easy local deployment
- ✅ Test suite for core functionality

## Tech Stack

- Python (88.7%)
- HTML (10.3%)
- Dockerfile (1.0%)

Key libraries (see requirements.txt):
- Django
- django-ninja
- psycopg2-binary

## Getting Started

### Prerequisites

- Python 3.8+
- pip (or poetry)
- Docker & docker-compose (optional, recommended for local containers)
- PostgreSQL (or use the Docker Compose service)

### Quickstart (local, virtualenv)

1. Clone the repository
   ```bash
   git clone https://github.com/DanPec-cmd/nano-bnpl.git
   cd nano-bnpl
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows (PowerShell)
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Set environment variables (example)
   Create a .env file or export variables:
   ```
   DJANGO_SECRET_KEY=your-secret-key
   DATABASE_URL=postgres://user:pass@localhost:5432/nanobnpl
   ```

5. Run migrations and start the server
   ```bash
   cd src
   python manage.py migrate
   python manage.py runserver
   ```

The API endpoints will be available on http://127.0.0.1:8000/ (see the transactions app for routes).

### Quickstart (docker-compose)

Build and run everything with Docker Compose:
```bash
docker-compose up --build
```
This will start the app and any declared services (e.g., PostgreSQL). Adjust environment variables in docker-compose.yml or a .env file as needed.

## Project Structure

```
nano-bnpl/
├── README.md
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── src/
    ├── manage.py
    ├── config/           # Django settings
    └── transactions/     # Django app (models, views, api, tests, templates)
```

## Running Tests

From the repository root:
```bash
cd src
python manage.py test
```
(Or run your preferred test runner if configured, e.g., pytest.)

## Contributing

Contributions are welcome. Please open issues or submit pull requests for bugs and features. If you plan to contribute, please:

- Fork the repo
- Create a descriptive branch
- Add tests for new behavior
- Open a PR with a clear description

## License

This project is open source — add your preferred license (e.g., MIT, Apache-2.0) to the repository if you want to clarify terms.

## Contact

For more information, visit the GitHub repository: https://github.com/DanPec-cmd/nano-bnpl

---

**Status**: Active Development
