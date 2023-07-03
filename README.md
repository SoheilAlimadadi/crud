# Running the Program and Testing the CRUD API

To run the program and test the CRUD API, follow the steps below:

## Step 1: Install Dependencies with Poetry

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to install the project dependencies using Poetry:

shell poetry install

This will create a virtual environment and install all the required dependencies specified in the `pyproject.toml` file.

## Step 2: Apply Database Migrations with Alembic

1. Make sure the database is properly configured in the project's configuration file.
2. Run the following command to apply the database migrations using Alembic:

shell alembic upgrade head

This will create the necessary database tables and schema based on the defined models.

## Step 3: Start the Server with Uvicorn

1. Run the following command to start the server using Uvicorn:

shell uvicorn main:app --reload

This will start the server and enable auto-reloading for code changes.

## Step 4: Test the CRUD API

1. Open a web browser and go to [https://127.0.0.1:8000/docs](https://127.0.0.1:8000/docs).
2. This will open the Swagger UI interface, which provides a user-friendly way to test the CRUD API.
3. Use the provided endpoints and parameters to perform various CRUD operations on the student data.
4. Make sure to provide valid input data and follow the API documentation for correct usage.

That's it! You can now run the program, apply the database migrations, start the server, and test the CRUD API using the Swagger UI interface. Enjoy!
