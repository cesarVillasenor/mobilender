# MobilinderTest

Prueba de programacion

> CSS Framework `Materialize`
> 
> Diagrama Entidad relacion `/static/img/ERD.png` 

## Requisitos

> Python `3.x`
>
> Sqlite
> 
> docker
>
> Django Rest Framework

## Instalar Requermientos del  proyecto

Corre `pip install -r requirements/dev.txt` 

## Construccion

Corre `python manage.py migrate` para implementar las migraciones .

Corre `python manage.py loaddata data.json` para prellenar algunas tablas.

Corre `docker build . -t mobilender` para construir la imagen

Corre `docker compose-up `
## Corre pruebas unitarias (Django Test)

corre `python manage.py test`
