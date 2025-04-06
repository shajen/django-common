from django.conf import settings
from django.http import HttpResponseRedirect


def load_settings(request):
    return {
        "LANGUAGES": settings.LANGUAGES,
    }


def language(request, language):
    response = HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))
    if language in dict(settings.LANGUAGES):
        request.session["django_language"] = language
        response.set_cookie(
            settings.LANGUAGE_COOKIE_NAME,
            language,
            max_age=settings.LANGUAGE_COOKIE_AGE,
            path=settings.LANGUAGE_COOKIE_PATH,
            domain=settings.LANGUAGE_COOKIE_DOMAIN,
            secure=settings.LANGUAGE_COOKIE_SECURE,
            httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
            samesite=settings.LANGUAGE_COOKIE_SAMESITE,
        )
    return response
