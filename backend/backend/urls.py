from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import FileResponse
from django.urls import path, include
from pathlib import Path
from django.http import FileResponse, HttpResponse

from hotel import views


def home(request):
    file_path = Path(settings.BASE_DIR).parent / "index.html"
    return FileResponse(open(file_path, "rb"), content_type="text/html")
def robots(request):
    return HttpResponse(
        "User-agent: *\n"
        "Allow: /\n\n"
        "Sitemap: https://job-cqz6.onrender.com/sitemap.xml\n",
        content_type="text/plain"
    )

urlpatterns = [
    path("", home, name="home"),
    path("robots.txt", robots, name="robots"),
    path("admin/", admin.site.urls),

    path("api/", include("hotel.urls")),

    path("jobs/", views.jobs_page, name="jobs_page"),
    path("spa/", views.spa_page, name="spa_page"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.BASE_DIR / "static"
    )