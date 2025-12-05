# Expense Tracker (Dockerized Python + PostgreSQL)

## Overview
This is a Dockerized Expense Tracker built with Python and PostgreSQL. It demonstrates connecting a Python app to PostgreSQL, creating a table, inserting and reading rows, and running both services with Docker Compose on a custom network.

## Files
- `expense_tracker.py` - Python app
- `requirements.txt` - Python dependencies
- `Dockerfile` - Builds Python app image
- `docker-compose.yml` - Runs Python and PostgreSQL containers

## Run
1. `docker-compose up --build`
2. Interact with the app from the python container:
   - In a separate terminal: `docker exec -it expense_app sh`
   - Run: `python expense_tracker.py`
3. Check DB: `docker exec -it expense_postgres psql -U postgres -d expenses_db`

