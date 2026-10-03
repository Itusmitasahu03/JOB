# Bond_Desk

A searchable platform for:
- Spa Centre
- Massage
- Online Job
- Nearby Job
- Work From Home
- Part Time Job
- Full Time Job

## Local setup

From the `backend` folder:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open the frontend with VS Code Live Server or another static server.

## Render

Root Directory: `backend`

Build Command:
`pip install -r requirements.txt`

Start Command:
`gunicorn backend.wsgi:application`

## Data

Jobs and services are database records managed through Django Admin. This starter project intentionally does not fabricate real businesses or job vacancies. Add verified/genuine listings through `/admin/`.

## Google discoverability

The project includes crawlable HTML, descriptive titles, meta descriptions, canonical URLs, robots.txt and sitemap.xml. Submit the sitemap and important URLs in Google Search Console. Indexing and ranking are not guaranteed; avoid keyword stuffing or fake listings.
