# DjangoCRUD
Primer CRUD en Django de manera manual 

django-admin startproject nombreproyecto //Crea el proyecto o lo inicializa
python manage.py runserver //Inicializa el servidor local
python manage.py startapp {nombre_de_la_futura_tabla}
{
    pip3 install PyMySQL // Instala las extenciones de MySQL para python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME':  'testdjango',
            'USER': 'root',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '3306'

        }
    }
}
python manage.py makemigrations// Realiza las migraciones 
python manage.py migrate //Migra las tablas a la base de datos
python manage.py createsuperuser //Crea super usario