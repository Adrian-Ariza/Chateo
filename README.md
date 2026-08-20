# 💬 Chateo

Plataforma web de mensajería con sistema de autenticación de usuarios, desarrollada como proyecto durante mi carrera de Ingeniería de Sistemas. Permite a los usuarios registrarse, iniciar sesión y enviar mensajes a otros usuarios dentro de la plataforma.

## 📋 Descripción

Aplicación web desarrollada con **Django** (arquitectura monolítica, usando el sistema de templates de Django para el frontend), que permite la comunicación entre usuarios registrados mediante un sistema de mensajería y gestión de sesiones basada en cookies.

## ✨ Funcionalidades

- 🔐 Registro e inicio de sesión de usuarios (login/register)
- 🍪 Manejo de sesión mediante cookies
- 💌 Envío y recepción de mensajes entre usuarios
- 🗄️ Persistencia de datos con SQLite

## ⚠️ Limitaciones conocidas

Este proyecto fue desarrollado con fines de aprendizaje y quedó sin finalizar en su totalidad. Actualmente:

- Los mensajes **no se actualizan en tiempo real**: aunque el mensaje sí llega y se guarda correctamente para el usuario destinatario, es necesario **recargar la página** para visualizarlo.
- La idea original era resolver esto con **peticiones AJAX periódicas** (polling) para refrescar los mensajes sin recargar la página, pero por límites de tiempo el proyecto se presentó sin esa funcionalidad implementada.
- Próxima mejora planeada: implementar el polling con AJAX pendiente, o evolucionar directamente a una solución con **WebSockets** (Django Channels) para mensajería en tiempo real real.

## 🛠️ Tecnologías utilizadas

- Python / Django 5.2 (backend y frontend con templates de Django)
- SQLite (base de datos)
- HTML/CSS (templates y archivos estáticos)
- Pillow (procesamiento de imágenes)
- psycopg2 (driver PostgreSQL, preparado para producción)

**Dependencias principales:**
```
asgiref==3.8.1
Django==5.2
pillow==11.2.1
psycopg2==2.9.10
sqlparse==0.5.3
tzdata==2025.2
Unipath==1.1
```

## 🚀 Instalación y ejecución local

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/chat-platform-django.git
cd chat-platform-django

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Configurar variables de entorno / secret key
# Crea tu propio secret.json o archivo .env con tu SECRET_KEY de Django
# (ver sección "Configuración" más abajo)

# Aplicar migraciones
python manage.py migrate

# Levantar servidor
python manage.py runserver
```

La aplicación quedará disponible en `http://localhost:8000`.


## 📁 Estructura del proyecto

```
├── applications/     # Apps de Django (lógica de negocio, modelos, vistas)
├── Django_project/   # Configuración principal del proyecto (settings, urls)
├── media/            # Archivos subidos por usuarios (ej. fotos de perfil)
├── static/           # Archivos estáticos (CSS, JS, imágenes)
├── templates/        # Plantillas HTML (frontend)
├── manage.py
└── db.sqlite3
```

## 📌 Estado del proyecto

🚧 En pausa / no finalizado — desarrollado con fines académicos y de práctica.

## 👤 Autor

Desarrollado por Adrian Ariza Tapia como parte de mi formación en Ingeniería de Sistemas.

- LinkedIn: https://www.linkedin.com/in/adrian-ariza-tapia-41a4603b7/
- GitHub: [@Adrian-Ariza](https://github.com/Adrian-Ariza)
