<div align="center">

  # 🍪 Session Authentication

  **Session-Based Authentication for REST APIs**

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

</div>

---

## 📖 Description

This project implements session-based authentication on a Flask API. You will learn how cookies work, how to create and manage session IDs, and how to implement login/logout endpoints.

## 🎯 Learning Objectives

- What authentication means
- What session authentication means
- What cookies are and how to send/parse them
- How to create a session ID

## 🛠️ Technologies

- Python 3
- Flask
- REST API

## 🚀 Setup & Run

```bash
pip3 install -r requirements.txt
API_HOST=0.0.0.0 API_PORT=5501 python3 -m api.v1.app
```

## 📡 Routes

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/v1/status` | Returns the status of the API |
| `GET` | `/api/v1/stats` | Returns some stats of the API |
| `GET` | `/api/v1/users` | Returns the list of users |
| `GET` | `/api/v1/users/:id` | Returns a user based on the ID |
| `DELETE` | `/api/v1/users/:id` | Deletes a user based on the ID |
| `POST` | `/api/v1/users` | Creates a new user |
| `PUT` | `/api/v1/users/:id` | Updates a user based on the ID |
| `POST` | `/api/v1/auth_session/login` | Session login |
| `DELETE` | `/api/v1/auth_session/logout` | Session logout |

---

<div align="center">
  <a href="../README.md">⬅️ Back to main project</a>
</div>
