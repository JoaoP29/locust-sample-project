# locust-sample-project
just a showcase project of performance testing using a python framework called Locust

# Performance Testing with Locust Using the ReqRes API

This project contains a sample script to perform performance testing using [Locust](https://locust.io/) with the public [ReqRes API](https://reqres.in/). The ReqRes API simulates CRUD operations for users, making it an ideal choice for demonstrations and training sessions.

## Overview

The goal of this project is to demonstrate how to set up and execute performance tests with Locust by simulating various operations with the ReqRes API. The script includes tasks that perform the following actions:
- List users
- Create a user
- Update a user
- Delete a user

## API Details: ReqRes

- **Base Endpoint:** `https://reqres.in`
- **Routes:**
  - `GET /api/users` – Retrieves a list of users.
  - `POST /api/users` – Creates a new user.
  - `PUT /api/users/{id}` – Updates an existing user.
  - `DELETE /api/users/{id}` – Deletes a user.

## Prerequisites

- Python 3.7 or higher
- pip

## Installation

1. Clone this repository:
```bash
  git clone https://github.com/your-username/your-repository.git
  cd your-repository
```
2. (Optional but recommended) Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate   # For Linux/Mac
  venv\Scripts\activate      # For Windows
  ```
3. Install the required dependencies:
  ```bash
  pip install locust
  ```
## Project Structure
  ```
  .
  ├── locustfile.py    # Performance test script for the ReqRes API
  └── README.md
  ```
## How to Run the Tests

1. Start Locust with the ReqRes Host:
  ```bash
  locust -f locustfile.reqres.py --host https://reqres.in
  ```
2. Open your browser and navigate to https://localhost:8089
3. Configure the number of users and spawn as desired, then start the test.
