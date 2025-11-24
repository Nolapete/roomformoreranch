from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.apps import apps

admin.site.site_header = "roomformoreranch.com Administration"
admin.site.site_title = "roomformoreranch.com"
admin.site.index_title = "Room For More Ranch Admin Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("landing.urls")),
    path("goats/", include("goats.urls")),
    re_path(
        r"^favicon\.ico$",
        RedirectView.as_view(url="/static/images/favicon.ico", permanent=True),
    ),
    path("i18n/", include("django.conf.urls.i18n")),
    path("shop/", include(apps.get_app_config("oscar").urls[0])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    # Append the debug toolbar URLs to the existing list
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
