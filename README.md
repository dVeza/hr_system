# Demo HR System - CRUD API with DRF


## Setup
```
docker compose build
docker compose run web python manage.py migrate
docker compose run web python manage.py import_mock_data './MOCK_DATA.json'
docker compose run web python manage.py createsuperuser --email admin@example.com --username admin
docker compose up -d
```

Then visit http://0.0.0.0:8000/ 
Use the above created superuser to login and enjoy the browsable api

## Structure

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`employees` | GET | READ | Get all employees
`employees/:id` | GET | READ | Get a single employee
`employees`| POST | CREATE | Create a new employee
`employees/:id` | PUT | UPDATE | Update an employee
`employees/:id` | DELETE | DELETE | Delete an employee
`industries` | GET | READ | Get all industries
`industries/:id` | GET | READ | Get a single industry
`industries`| POST | CREATE | Create a new industry
`industries/:id` | PUT | UPDATE | Update an industry
`industries/:id` | DELETE | DELETE | Delete an industry
`stats/` | GET | READ | Stats by industry with get params
`stats2/` | GET | READ | Stats by industry
