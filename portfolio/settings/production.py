from .base import *

ALLOWED_HOSTS = [".portfolio.app.br", "www.portfolio.app.br", ".herokuapp.com", "127.0.0.1"]

# TODO MAKE USE OF THE AUTOMATIC UPDATED DATABASE_URL ENVIRONMENT VARIABLE FROM HEROKU
# THIS WAY YOU AUTOMATICALLY CHANGE HOST ALSO...

DATABASES = {
    "prod": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PWD"),
        "HOST": "blablabla.amazonaws.com",
        "PORT": "5432",
    },
    "dev": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

DATABASES["default"] = DATABASES["dev" if DEVELOPMENT else "prod"]

DOMAIN_URL_STRIPE = "http://127.0.0.1:8000" if DEVELOPMENT else "http://www.portfolio.app.br"

DEBUG_PROPAGATE_EXCEPTIONS = True
