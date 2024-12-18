# FastAPI Clean Architecture Project

## Introduction
This repository demonstrates a clean architecture implementation using FastAPI. The project is designed to separate concerns, maintain scalability, and improve code readability. Developers can use this structure as a foundation for building robust and maintainable backend services.

---

## Project Structure
The project follows a modular and layered structure to enforce clean architecture principles. Below is an overview of the folder hierarchy:

```
.gitignore
Dockerfile
docker-compose.yml
requirements.txt
src/
├── bin/                # Command-line interface and script entry points
├── configs/            # Configuration files or placeholders
├── controllers/        # API route handlers and controllers
├── main.py             # Application entry point
├── models/             # Data models and exceptions
├── requests/           # Request schemas and validation logic
├── responses/          # Response schemas and formatting
├── services/           # Business logic and service layers
└── utils/              # Utility functions and helpers
```

### Key Notes
- **Code Organization**: All source code is under the `src` directory to keep the root clean and avoid module name conflicts.
- **Modular Design**: The project is divided into modules like `controllers`, `services`, and `models` to separate concerns and ensure scalability.
- **Versioning**: Controllers are versioned (e.g., `v1_user_controller.py`, `v2_user_controller.py`) to allow for API evolution without breaking existing clients.

---

## Contribution
Any recommendations or tips are welcome. You can either create a pull request or open an issue.

---