
# Services Tree 🌳

Services Tree is a simple, yet powerful REST API designed to manage my homelab services.

> **Note**: This is a **hobby project**

## Features

- **CRUD Operations**: Create, Read, Update, and Delete services.
- **OpenAPI Documentation**: Auto-generated documentation (Thanks to FastAPI).
- **Docker Compose Integration**: Easily set up the environment with Docker Compose.
- **Dependency Management**: Managed with Poetry 

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/M3nin0/services-tree.git
cd services-tree
```

2. Run using Docker Compose:

```bash
docker-compose up -d
```

This command builds the Docker image and starts the services defined in your `docker-compose.yml`, making the API accessible on the defined port (usually `http://localhost:8000`).

### Accessing the Documentation

Once the server is running, you can access the OpenAPI documentation by navigating to `/docs` in your web browser. This page will provide you with an interactive UI to test and explore the API's capabilities.

## Testing

To run tests, use the following command:

1. Clone the repository:

```bash
git clone https://github.com/M3nin0/services-tree.git
cd services-tree
```

2. Install dependencies with Poetry:

```bash
poetry install --with dev
```

3. Configure the database

```bash
alembic upgrade head
```

4. Test!

```bash
poetry run pytest
```

This command executes the test suite defined with pytest, ensuring that your API's functionality is verified.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.
