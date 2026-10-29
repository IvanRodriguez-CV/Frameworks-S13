# Semana 13 - CRUD y paginación

Proyecto Django de las guías de Semana 13: productos relacionados con
categorías, carga opcional de imágenes y paginación de diez productos por
página.

## Preparar el entorno

En PowerShell, desde esta carpeta:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Configura MySQL o MariaDB y crea una base de datos llamada `comercial`. La
conexión usa estas variables de entorno; si no las defines, usa `root` sin
contraseña en `127.0.0.1:3306`:

```powershell
$env:DB_NAME = "comercial"
$env:DB_USER = "root"
$env:DB_PASSWORD = "tu contraseña"
$env:DB_HOST = "127.0.0.1"
$env:DB_PORT = "3306"
```

Django 6.1 requiere Python 3.12 o posterior y MariaDB 10.11 o posterior.

## Migraciones y servidor

```powershell
python .\manage.py migrate
python .\manage.py runserver
```

Administra categorías en <http://127.0.0.1:8000/categoria/> y productos en
<http://127.0.0.1:8000/producto/>.

Las imágenes JPG y PNG se guardan en `media/productos/`. El formulario valida
que el precio de venta sea mayor que el precio de compra. El listado pagina
diez productos por página.

Para ejecutar las pruebas locales sin MySQL o MariaDB:

```powershell
$env:DB_ENGINE = "sqlite"
python .\manage.py test catalogo
```

La migración `0007_remove_unrelated_models` retira del estado de Django los
modelos `Cliente`, `Rol` y `TipoPago`, ajenos a estas guías, sin borrar sus
tablas ni sus datos existentes.
