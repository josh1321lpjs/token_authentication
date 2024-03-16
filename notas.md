### Comandos de entorno virtual en python
    -***python3 -m venv venv***

### Comandos de Django REST Framework

1. Inicializar dependencias del proyecto
    - ***pip install djangorestframework python-dotenv***
    - ***pip install django-cors-headers***

Install from pip [django-cors-headers](https://pypi.org/project/django-cors-headers/ "Title") Setup.

Install from pip [psycopg2](https://pypi.org/project/psycopg2/ "Title") Setup.

    - *** pip freeze > requirements.txt***
    
3. Crear un proyecto de django
    - ***django-admin startproject token_auth .***
4. Añadir aplicación 
    - ***python3 manage.py startapp users***
5. Crear archivo en el directorio raíz 
    - ***.env.local***
6. Crear migraciones 
    - ***python3 manage.py makemigrations***
7. Crear migraciones 
    - ***python3 manage.py migrate***
8. Ejecutar servidor  
    - ***python3 manage.py runserver***    
9. Agregar git
    - ***python3 manage.py runserver***
```
código
```