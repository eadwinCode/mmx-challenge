from momox.settings.base import *

SQL_DB = {"ENGINE": "django.db.backends.sqlite3", "NAME": "db.sqlite3"}

INSTALLED_APPS += [
    # ...
    'debug_toolbar',
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

MIDDLEWARE += [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # ...
]

POSTGRES_DB = {
    "ENGINE": "django.db.backends.postgresql_psycopg2",
    "NAME": os.getenv("POSTGRES_DB"),
    "USER": os.getenv("POSTGRES_USER"),
    "PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    "HOST": os.getenv("POSTGRES_HOST"),
    "PORT": os.getenv("POSTGRES_PORT"),
    "ATOMIC_REQUESTS": True,
}
DATABASES = {
    "default": POSTGRES_DB if os.getenv("POSTGRES_DB") else SQL_DB
}

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)s] %(module)s %(process)d %(thread)d %("
                          "message)s",
            },
        },
        "handlers": {
            "console": {"class": "logging.StreamHandler", "formatter": "console", },
        },
        "loggers": {
            "": {"level": LOG_LEVEL, "handlers": ["console", ], },
            'django.db': {
                'level': 'DEBUG',
                'handlers': ['console'],
            }
        },
    }
)

EMAIL_BACKEND = (
    "django.core.mail.backends.console.EmailBackend"
)
