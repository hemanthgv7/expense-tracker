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
 
________________________________________
Step 4: Running the Setup
We started both containers using:
docker-compose up --build
The output showed:
--- Expense Tracker (PostgreSQL Version) ---
1. Add Expense
2. View Expenses
At this point, the Python app was successfully connected to PostgreSQL.
 

________________________________________
Step 5: Validating Data Inside PostgreSQL
To check whether our Python app really saved data, we opened PostgreSQL inside the container:
docker exec -it expense_postgres psql -U postgres -d expenses_db
Inside the SQL shell, we ran:
List all tables
\dt
View expense table data
SELECT * FROM expenses;
Seeing the stored rows confirmed that:
•	Our database is running properly
•	Python successfully connects and inserts data
•	Docker networking works perfectly

 



