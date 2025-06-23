# IAM Employee Management

A simple Employee Management REST API built with FastAPI and SQLAlchemy.

## Features
- Add, view, update, and delete employees
- SQLite database integration
- Pydantic models for data validation

## Employee Table Schema

| Field | Type    | Notes                  |
|-------|---------|------------------------|
| id    | Integer | Primary key, auto-inc. |
| name  | String  | Employee name          |
| email | String  | Unique, required       |
| dept  | String  | Department name        |

## API Endpoints

- `GET /emp` — List all employees
- `GET /emp/{emp_id}`- List one employee
- `POST /emp` — Add a new employee
- `PUT /emp/{emp_id}` — Update an employee by ID
- `DELETE /emp/{emp_id}` — Delete an employee by ID

## Example Request (Add Employee)
```json
POST /emp
{
  "name": "John Doe",
  "email": "john@example.com",
  "dept": "Engineering"
}
```

---

Feel free to extend this project for your own use cases! 