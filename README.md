# Project instructions

## Project dependancies

| Name           | Version  |
|:--------------:|:--------:|
| Python         | 3.11     |
| FastAPI        | 0.99.0   |
| SQLAlchemy     | ^2.0.17  |
| psycopg        | 3.1.9    |
| alembic        | ^1.11.1  |

## Running the Program CRUD API

After cloning the project, follow the steps below:

### Step 1: Install Dependencies with Poetry

(install poetry if you don't have it, install instructions: [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation))

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to install the project dependencies using Poetry:

```bash
poetry install
```

This will create a virtual environment and install all the required dependencies specified in the `pyproject.toml` file.

the venv should be activated but if it doesn't, run the following command:

```bash
poetry shell
```

### step 2: create the database and add info to settings.toml inside the root of the project

in the terminal-based front-end to PostgreSQL called psql, copy and paste the following commands
(you can change the values if needed, or add a more secure password, this is just a dem)

```sql
CREATE DATABASE crud; CREATE USER crud_user WITH PASSWORD 'password'; ALTER ROLE crud_user SET client_encoding TO 'utf8'; ALTER ROLE crud_user SET default_transaction_isolation TO 'read committed'; ALTER ROLE crud_user SET timezone TO 'UTC'; ALTER USER crud_user CREATEDB; ALTER USER crud_user LOGIN; ALTER DATABASE crud OWNER TO crud_user; ALTER ROLE crud_user WITH CREATEDB; GRANT ALL PRIVILEGES ON DATABASE crud TO crud_user; grant usage on schema public to crud_user; grant create on schema public to crud_user;
```

if you change the values of db name, user and password, remember to change them also in the settings.toml
(in a real project settings.toml should be added to .gitignore)

### Step 3: Apply Database Migrations with Alembic

1. Make sure the database is properly configured in the project's configuration file.
2. Run the following command to apply the database migrations using Alembic:

```bash
alembic upgrade head
```

This will create the necessary database tables and schema based on the defined models.

### Step 4: Start the Server with Uvicorn

1. Run the following command to start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

This will start the server and enable auto-reloading for code changes.

### Step 5: Test the CRUD API

1. Open a web browser and go to [https://127.0.0.1:8000/docs](https://127.0.0.1:8000/docs).
2. This will open the Swagger UI interface, which provides a user-friendly way to test the CRUD API.
3. Use the provided endpoints and parameters to perform various CRUD operations on the student data.
4. Make sure to provide valid input data and follow the API documentation for correct usage.

That's it! You can now run the program, apply the database migrations, start the server, and test the CRUD API using the Swagger UI interface. Enjoy!
