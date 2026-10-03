from django.shortcuts import render
import json

from django.http import JsonResponse
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import Job, Service


def search_jobs(request):
    search = request.GET.get("search", "").strip()
    location = request.GET.get("location", "").strip()
    job_type = request.GET.get("type", "").strip()

    jobs = Job.objects.all()

    if search:
        jobs = jobs.filter(
            Q(title__icontains=search)
            | Q(company__icontains=search)
            | Q(location__icontains=search)
            | Q(job_type__icontains=search)
            | Q(work_mode__icontains=search)
            | Q(skills__icontains=search)
            | Q(description__icontains=search)
        )

    if location:
        for word in location.replace(",", " ").split():
            if len(word) >= 2:
                jobs = jobs.filter(
                    Q(location__icontains=word)
                    | Q(title__icontains=word)
                    | Q(company__icontains=word)
                )

    if job_type:
        jobs = jobs.filter(job_type__iexact=job_type)

    data = [{
        "id": j.id,
        "title": j.title,
        "company": j.company,
        "location": j.location,
        "job_type": j.job_type,
        "work_mode": j.work_mode,
        "salary": j.salary,
        "skills": j.skills,
        "description": j.description,
        "application_link": j.application_link,
        "created_at": j.created_at.strftime("%d %b %Y"),
    } for j in jobs]

    return JsonResponse(data, safe=False)


def job_detail(request, job_id):
    try:
        j = Job.objects.get(id=job_id)
    except Job.DoesNotExist:
        return JsonResponse({"error": "Job not found"}, status=404)

    return JsonResponse({
        "id": j.id, "title": j.title, "company": j.company,
        "location": j.location, "job_type": j.job_type,
        "work_mode": j.work_mode, "salary": j.salary,
        "skills": j.skills, "description": j.description,
        "application_link": j.application_link,
        "created_at": j.created_at.strftime("%d %b %Y"),
    })


@csrf_exempt
def add_job(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        data = json.loads(request.body)
        job = Job.objects.create(
            title=data["title"], company=data["company"],
            location=data["location"], job_type=data["job_type"],
            work_mode=data.get("work_mode", ""),
            salary=data.get("salary", ""), skills=data.get("skills", ""),
            description=data.get("description", ""),
            application_link=data.get("application_link", ""),
        )
        return JsonResponse({"message": "Job added", "id": job.id}, status=201)
    except (KeyError, json.JSONDecodeError) as e:
        return JsonResponse({"error": str(e)}, status=400)


def search_services(request):
    search = request.GET.get("search", "").strip()
    location = request.GET.get("location", "").strip()
    service_type = request.GET.get("type", "").strip()

    services = Service.objects.all()
    if search:
        services = services.filter(
            Q(name__icontains=search)
            | Q(location__icontains=search)
            | Q(service_type__icontains=search)
            | Q(description__icontains=search)
        )
    if location:
        for word in location.replace(",", " ").split():
            if len(word) >= 2:
                services = services.filter(
                    Q(location__icontains=word) | Q(name__icontains=word)
                )
    if service_type:
        services = services.filter(service_type__iexact=service_type)

    data = [{
        "id": s.id, "name": s.name, "service_type": s.service_type,
        "location": s.location, "phone": s.phone,
        "description": s.description, "price_from": s.price_from,
        "website": s.website,
    } for s in services]
    return JsonResponse(data, safe=False)


def service_detail(request, service_id):
    try:
        s = Service.objects.get(id=service_id)
    except Service.DoesNotExist:
        return JsonResponse({"error": "Service not found"}, status=404)
    return JsonResponse({
        "id": s.id, "name": s.name, "service_type": s.service_type,
        "location": s.location, "phone": s.phone,
        "description": s.description, "price_from": s.price_from,
        "website": s.website,
    })


@csrf_exempt
def add_service(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        data = json.loads(request.body)
        s = Service.objects.create(
            name=data["name"], service_type=data["service_type"],
            location=data["location"], phone=data.get("phone", ""),
            description=data.get("description", ""),
            price_from=data.get("price_from", ""),
            website=data.get("website", ""),
        )
        return JsonResponse({"message": "Service added", "id": s.id}, status=201)
    except (KeyError, json.JSONDecodeError) as e:
        return JsonResponse({"error": str(e)}, status=400)
def spa_page(request):
    return render(request, "spa.html")
def home_page(request):
    return render(request, "index.html")
def jobs_page(request):
    return render(request, "jobs.html")