from django.conf import settings

if getattr(settings, 'ALGOLIA', {}).get('APPLICATION_ID') is not None:
    default_app_config = 'api.apps.ApiConfig'