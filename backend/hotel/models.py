from django.db import models

class Job(models.Model):
    JOB_TYPES = [
        ("Online Job", "Online Job"),
        ("Nearby Job", "Nearby Job"),
        ("Work From Home", "Work From Home"),
        ("Part Time Job", "Part Time Job"),
        ("Full Time Job", "Full Time Job"),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOB_TYPES)
    work_mode = models.CharField(max_length=100, blank=True)
    salary = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=500, blank=True)
    description = models.TextField()
    application_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title} - {self.location}"


class Service(models.Model):
    SERVICE_TYPES = [
        ("Spa Centre", "Spa Centre"),
        ("Massage", "Massage"),
    ]

    name = models.CharField(max_length=200)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50, blank=True)
    description = models.TextField()
    price_from = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} - {self.location}"
