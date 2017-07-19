import os

STATIC_URL = '/static/'
STATIC_ROOT = '/code/static/'
ALLOWED_HOSTS = [host.strip() for host in os.environ.get("ALLOWED_HOSTS", '').split(',')]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME', 'postgres'),
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'HOST': os.environ.get('DATABASE_HOST', 'db'),
        'PORT': 5432,
    }
}
db_password = os.environ.get('DATABASE_PASSWORD', False)
if db_password:
    DATABASES.get('default').update({'PASSWORD': db_password})

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100
}

if os.environ.get('ALGOLIA_APPLICATION_ID', None) is not None:
    INSTALLED_APPS.append('algoliasearch_django')
    ALGOLIA = {
        'APPLICATION_ID': os.environ.get('ALGOLIA_APPLICATION_ID', None),
        'API_KEY': os.environ.get('ALGOLIA_API_KEY', None)
    }
