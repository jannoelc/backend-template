# Backend Template

This is a headless Django app that serves as the backend for [frontend-template](https://github.com/jannoelc/frontend-template).

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

## Built With

- [Django](https://docs.djangoproject.com/en/5.2/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Django All Auth](https://docs.allauth.org/en/latest/)
- [PostgreSQL](https://www.postgresql.org/) (though this should work with any database supported by Django ORM)

## Setup

This repository was initially built with the [Cookiecutter Django](https://cookiecutter-django.readthedocs.io/en/latest/) template, so most of the documentation there also applies to this project.

### Running Locally with Docker (Preferred)

This is the preferred approach since you can get started in seconds as long as you have Docker installed.

**Requirements:**

- Docker
- [Just](https://github.com/casey/just) (optional)

The instructions below assume that you have installed `Just`. It is a convenient way to run commands instead of always typing `docker compose -f docker-compose.local.yml`. If not, use the `justfile` in the root directory as a reference.

1. Assuming you are in the root folder, run the command below. This will install all the pip dependencies and build the base Docker image:

   ```bash
   just build
   ```

2. Run the migration scripts:

   ```bash
   just manage migrate
   ```

3. Run the Docker Compose stack. The Django Dockerfile includes a file watcher, so any changes made to the code will automatically restart the Django app:

   ```bash
   just up
   ```

4. You may view the logs in real time by running:

   ```bash
   just logs <app_name or leave blank to view all>
   ```

To stop the Docker Compose stack, run:

```bash
just down
```

To delete the entire stack (e.g., if there are issues with database data, migrations, or builds), run:

```bash
just prune
```

#### Caveat

Currently, there is no way to install dependencies via `pip install`. As a workaround, add the dependency to `requirements.txt` and run `just build`.

### Running Locally

_Support for this is limited for now. The steps for running this locally have not been fully verified compared to the Docker-based version._

See the documentation on running this locally [here](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally.html). Skip the parts on generating a new project.

## Migrations

For running migrations, see the [Django migrations documentation](https://docs.djangoproject.com/en/5.2/topics/migrations).

If you are developing locally with Docker, replace `python manage.py` with `just manage`:

```bash
just manage migrate
just manage makemigrations
just manage sqlmigrate
just manage showmigrations
```

## Settings

Settings are segregated into the following files:

- `config/settings/base.py` - Common settings
- `config/settings/local.py` - Local-only settings
- `config/settings/test.py` - Test-only settings
- `config/settings/prod.py` - TODO

### Environment Variables

Only local environment files are available for now in `.env/.local/*`.

## Dev Tools

### PG Admin

PG Admin is included in the Docker Compose stack, although you have to manually get the host and port of your Postgres Docker instance using the commands below:

1. Get the list of Docker networks:

   ```bash
   docker network ls
   ```

2. Look for the ID of the Docker network that matches your stack, and view its details:

   ```bash
   docker network inspect <name or ID>
   ```

3. Look for the entry for `apps_local_postgres` and use the IP address as the host, and `5432` as the port.

### Mailpit

In development, it is often useful to see emails sent from your application. For that reason, the local SMTP server [Mailpit](https://github.com/axllent/mailpit) with a web interface is available as a Docker container.

The Mailpit container will start automatically when you run all Docker containers. Please check the [Cookiecutter Django Docker documentation](https://cookiecutter-django.readthedocs.io/en/latest/2-local-development/developing-locally-docker.html) for more details on how to start all containers.

With Mailpit running, to view messages sent by your application, open your browser and go to `http://localhost:8025`.

### Swagger/OpenAPI

While the application is running, Swagger/OpenAPI documentation is available at:

| Service         | Documentation URL                     |
|------------------|---------------------------------------|
| Authentication  | `http://localhost:8000/api/auth/openapi.html` |
| Backend         | `http://localhost:8000/api/docs/`     |

Unfortunately, due to CSRF and cookie implementation, the backend Swagger page cannot be used directly yet without turning off a couple of settings.

**TODO:** Expose a setting or an environment variable to disable cookie session IDs and CSRF tokens when working locally.

## Architectural Choices

### Authentication

This project leverages the well-established [Django All Auth](https://docs.allauth.org/en/latest/) library for authentication. Key benefits include:

- **Reduced Development Time**: By using a pre-built library, developers can focus on core application features instead of building authentication from scratch.
- **Enhanced Security**: Django All Auth is widely adopted and actively maintained, ensuring adherence to robust security practices.
- **Extensibility**: It supports multiple authentication methods, including social logins, making it easy to expand functionality as the project grows.

### Backend Architecture

The project is built using Django and Django REST Framework, which provide a solid foundation for rapid development and maintainability. Key advantages include:

- **Rapid Prototyping**: Django's built-in ORM and admin interface simplify database management and accelerate development.
- **REST API Support**: Django REST Framework offers powerful tools like serializers, viewsets, and built-in authentication, streamlining the creation of RESTful APIs.
- **Modular Design**: The app-based structure of Django promotes separation of concerns, making the codebase easier to maintain and scale.
