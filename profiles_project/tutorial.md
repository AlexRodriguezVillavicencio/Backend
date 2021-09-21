******************************************************
            CREANDO UN LOGIN CON EMAIL PARA USUARIO
******************************************************
1.INSTALACION DE PAQUETES

2.CREACIÓN DE PROYECTOS

*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.CONFIGURANDO EL SETTING
-.---------------------------------------------------.-
Importamos en <profiles_project/settings.py> nuestra aplicación y el rest_framework:

            INSTALLED_APPS = [
                    ...
                'rest_framework',
                'rest_framework.authtoken'
                'profiles_api'
            ]

Lo que haremos ahora es crear un modelo de usuario dentro de la aplicación <profiles_api/models.py>:

            from django.db import models
            from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

            class UserProfile(AbstractBaseUser,PermissionsMixin):
                        ...

*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.AGREGANDO MANAGER DE USUSARIO
-.---------------------------------------------------.-
luego de crear nuestro primer modelo de ususario personalizado, tenemos que especificar como vamos a procesar nuestros ususario.
Para eso vamos a trabajar el <UserProfileManager> dentro del mismo models.py, de la clase UserProfile:

            from django.contrib.auth.models import BaseUserManager

            class UserProfileManager(BaseUserManager):
                        ....

*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.MODELO DE USUARIO PERSONALIZADO
-.---------------------------------------------------.-
Ahora que hemos creado el perfil de usuario y el manager usuario, ahora le decimos a django que esto es lo que queremos utilizar.
para hacer esto modificamos el archivo <profiles_project/setting.py> y al ultimo de las lineas de codigo definimos:

                    ...
                    
            AUTH_USER_MODEL = 'profiles_api.UserProfile'

este modelo que hemos hecho lo vamos usar para autenticacion y registro de ususarios.
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.MIGRACIONES DE BASE DE DATOS
-.---------------------------------------------------.-
vamos a hacer las migraciones, para hacer un match entre el archivo del models.py y nuestro base de datos:

>python manage.py makemigrations
>python manage.py migrate
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
luego creamos nuestro super usuario:

>python manage.py createsuperuser
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.ACCESO ADMIN Y PROBANDO ADMIN
-.---------------------------------------------------.-
vamos a habilitar el modelo que hemos creado en la pagina de admin.
Nos ubicamos en <profiles_api/admin.py>:

            from django.contrib import admin
            from profiles_api import models

            admin.site.register(models.UserProfile)

una vez hecho ello, corremos nuestro servidor con:
>python manage.py runserver

Dentro del panel de administración, el authtoken nos permite tener accseo a los tokens.

*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.CREANDO PRIMER APIView
-.---------------------------------------------------.-
Nos vamos al archivo <profiles_api/views.py>

*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-
