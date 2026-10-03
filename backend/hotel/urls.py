from django.urls import path
from . import views

urlpatterns = [
    # Jobs API
    path("jobs/", views.search_jobs, name="search_jobs"),
    path("jobs/<int:job_id>/", views.job_detail, name="job_detail"),
    path("jobs/add/", views.add_job, name="add_job"),

    # Services API
    path("services/", views.search_services, name="search_services"),
    path("services/<int:service_id>/", views.service_detail, name="service_detail"),
    path("services/add/", views.add_service, name="add_service"),
]