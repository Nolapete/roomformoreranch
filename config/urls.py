"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    # Append the debug toolbar URLs to the existing list
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
