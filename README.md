# Enterprise E-Commerce API

## Features

- JWT Authentication
- Role Based Access
- Product CRUD
- Order Management
- Product Search
- Pagination
- Docker Support
- Swagger Documentation

## Tech Stack

- FastAPI
- SQLAlchemy
- MySQL
- JWT
- Docker
- Alembic

## Run Project

pip install -r requirements.txt
uvicorn main:app --reload

## Docker

docker compose -f docker/docker-compose.yml up --build

## API Docs

http://localhost:8000/docs