from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from hotel import views


urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # API
    path("api/", include("hotel.urls")),

    # Website pages
    path("", views.home_page, name="home"),
    path("jobs/", views.jobs_page, name="jobs_page"),
    path("spa/", views.spa_page, name="spa_page"),
]


# Serve static files during local development
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.BASE_DIR / "static"
    )