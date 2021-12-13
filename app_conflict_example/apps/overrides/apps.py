from django.contrib.auth.apps import AuthConfig


class CustomDjangoAuthConfig(AuthConfig):
    verbose_name = "Custom Auth"
    label = "django_auth"
