# FastAPI CRUD Application

This repository contains a **full-stack CRUD application** built to understand and demonstrate real-world backend and frontend development concepts.

The project focuses on building **RESTful APIs using FastAPI**, integrating a **PostgreSQL database**, connecting it with a **React-based frontend**, and implementing **Docker containerization and Jenkins CI/CD pipeline** for automated build and deployment.

The goal of this project is to practice **API design, database operations, frontend-backend communication, containerization, and CI/CD automation** in a structured and practical way.

---

# 🚀 What this project demonstrates

How to build REST APIs using **FastAPI**

How CRUD operations work in real applications

How to connect FastAPI with **PostgreSQL using SQLAlchemy**

How a **React frontend communicates with backend APIs**

How **CORS works in frontend-backend architecture**

How to containerize an application using **Docker**

How to implement **CI/CD automation using Jenkins**

How to manage a full-stack project using **Git & GitHub**

---

# ✨ Features

Create, Read, Update, and Delete (CRUD) operations

RESTful API structure

PostgreSQL database integration

React-based frontend interface

CORS enabled for cross-origin requests

Dockerized backend application

Automated build and deployment using Jenkins pipeline

Clean and beginner-friendly project structure

---

# 🛠 Tech Stack

## Backend

FastAPI (Python)

SQLAlchemy

PostgreSQL

Uvicorn

---

## Frontend

React

JavaScript

HTML

CSS

---

## DevOps / Deployment

Docker

Jenkins (CI/CD Pipeline)

Docker Containers

---

## Tools & Version Control

Git

GitHub

---

# 📂 Project Structure

```
fastAPI-CRUD-Project/

│
├── main.py
├── models.py
├── database.py
├── mockData.py
├── database_models.py
│
├── Dockerfile
├── Jenkinsfile
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone the Repository

```
git clone https://github.com/abhishek830-dev/fastAPI-CRUD-Project.git

cd fastAPI-CRUD-Project
```

---

# 🖥 Backend Setup

Create virtual environment

```
python -m venv myenv
```

Activate environment

```
myenv\Scripts\activate
```

Install dependencies

```
pip install fastapi uvicorn sqlalchemy psycopg2
```

Run FastAPI server

```
uvicorn main:app --reload --env-file .env
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend Setup

Navigate to frontend folder

```
cd frontend
```

Install dependencies

```
npm install
```

Start React application

```
npm start
```

Frontend will run at:

```
http://localhost:3000
```

---

# 🐳 Running the Application using Docker

Build Docker image

```
docker build -t fastapi-crud-app .
```

Run Docker container

```
docker run -d -p 8000:8000 --name fastapi-container fastapi-crud-app
```

The API will be available at:

```
http://localhost:8000
```

Swagger Documentation:

```
http://localhost:8000/docs
```

---

# ⚙️ CI/CD Pipeline using Jenkins

This project includes a **Jenkins pipeline** to automate the build and deployment process.

## Jenkins Pipeline Workflow

```
GitHub Repository
        ↓
Jenkins Pipeline Trigger
        ↓
Build Docker Image
        ↓
Stop Existing Container
        ↓
Deploy New Container
        ↓
Application Available on Port 8000
```

### Jenkinsfile automates:

• Pulling the latest code from GitHub
• Building a Docker image
• Stopping any existing container
• Running a new container with the updated image

This demonstrates a **basic CI/CD pipeline used in real-world DevOps workflows.**

---

# 🔗 API Endpoints (Examples)

GET /products – Fetch all products

POST /products – Create a new product

PUT /products/{id} – Update an existing product

DELETE /products/{id} – Delete a product

---

# 🎯 Purpose of This Project

This project was built primarily for **learning and hands-on practice**, with a focus on:

Backend development using FastAPI

Database design and operations

Frontend and backend integration

Understanding containerization using Docker

Implementing CI/CD automation using Jenkins

Understanding real-world development workflow

---

# 📄 License

This project is licensed under the **MIT License**.
