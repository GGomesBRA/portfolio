# STARTING THE PROJECT

```bash
py -m venv venv
.\venv\scripts\activate
pip install django
django-admin startproject facilit
```

    create settings folder
    change base.py to use base folder for settings
    use DEBUG base variable in manage.py to select local or production settings
    create requirements.txt

## INSTALLED PACKAGES

```bash
pip install django==4.2.5
pip install python-dotenv==1.0.0
pip install djangorestframework==3.14.0
pip install pytest==7.4.2
pip install gunicorn==21.2.0
pip install whitenoise==6.6.0
pip install psycopg2=2.9.9
pip install django-allauth==0.57.0
pip install pandas==2.1.2
pip install Pillow=10.1.0
```

## RESETING MIGRATIONS AND DB

```bash
rm -r db.sqlite3; rm -r ./facilit/dashboard/migrations; rm -r ./facilit/profiles/migrations; rm -r ./facilit/public/migrations; rm -r ./facilit/staff/migrations; rm -r ./facilit/subscriptions/migrations; rm -r ./facilit/sefaz/migrations; rm -r ./facilit/sped/migrations
```

```bash
py manage.py makemigrations dashboard --empty; py manage.py makemigrations profiles --empty; py manage.py makemigrations public --empty;  py manage.py makemigrations staff --empty;  py manage.py makemigrations subscriptions --empty;  py manage.py makemigrations sefaz --empty;  py manage.py makemigrations sped --empty;  py manage.py makemigrations; py manage.py migrate --run-syncdb; py manage.py runscript cfop; py manage.py runscript ajustes; py manage.py createsuperuser; py manage.py runserver
```
