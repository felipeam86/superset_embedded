# Demo app for embedding Superset dashboards

This is a simple demo app for testing superset embedded dashboards.

## Prepare environment

For a simple setup:

```bash
 pip install fastapi python-dotenv requests
```

This code was developed on Python 3.9 with [Poetry](https://python-poetry.org/) as
dependency manager. If you want to reproduce the development environment, do
`poetry install` to prepare an isolated development environment or
`pip install -r requirements.txt` with your prefered environment manager

## Set up environment variables

Create a file named `.env` with the following environment variables:

```
API_TOKEN=<API_TOKEN>
SECRET=<SECRET>
URL_AUTH=<URL_AUTH>
URL_GUEST_TOKEN=<URL_GUEST_TOKEN>
USERNAME=<USERNAME>
FIRST_NAMER=<FIRST_NAMER>
LAST_NAME=<LAST_NAME>
DASHBOARD_ID=<DASHBOARD_ID>
SUPERSET_DOMAIN=<SUPERSET_DOMAIN>
```

## Running the app

To run the app, do the following command:
```bash
uvicorn main:app --reload
```

The app is now running at [localhost:8000/](http://localhost:8000/)
