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

            from rest_framework.views import APIView
            from rest_framework.response import Response

            class HelloApiView(APIView):    
                      ...

*******************************************************
3.URL DE API VIEW
-.---------------------------------------------------.-
ahora que tenemos nuestro view, podemos crear nuestra url para poder ver esta api view.
creamos un <urls.py> dentro de nuestra aplicación

            from django.urls import path
            from profiles_api import views

            urlpatterns = [
                path('hello-view/',views.HelloApiView.as_view())

lo conectamos con el <urls.py> del proyecto

            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('api/', include('profiles_api.urls'))
            ]

ya podemos ver nuestra api rest en la url creada
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.CREAR SERIALIZADOR
-.---------------------------------------------------.-
nos permite convertir objectos de python a json y viceversa.
Entonces los metodos los crearemos en nuestro serializador, 
para eso creamos un archivo <serializers.py> dentro de la aplicacion.

            from rest_framework import serializers

            class HelloSerializer(serializers.Serializer):
                name = serializers.CharField(max_lenght=10)

ahora que hemos creado nuestro serializador, proecedemos a crear nuestro primer metodo POST, para eso nos vamos a <views.py>
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.CREANDO LOS METODOS POST , PUT Y DELETE
-.---------------------------------------------------.-
en el archivo de <views.py> deficinimos nuestras funciones par post:

            from rest_framework import serializers, status
            from profiles_api import serializers

                ...

            def post(self,request):        
                    serializer = self.serializer_class(data=request.data)

                    if serializer.is_valid():          
                        name = serializer.validated_data.get('name') 
                        message = f'hola {name}'
                        return Response({'message':message})
                    
                    else:         
                        return Response(
                            serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                        )
de la misma manera creamos funciones para los siguientes metodos, que estan mas detallados en
el archivi views.py.
*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.INTRODUCCIÓN A LOS VIEWSET
-.---------------------------------------------------.-
nos vamos al archivo <views.py> y creamos una nueva clase para porbar los viewSet

            from rest_framework import viewsets

                    ...

            class HelloViewSet(viewsets.ViewSet):

*******************************************************
3.AGREGANDO URL ROUTER
-.---------------------------------------------------.-
nos vamos al archivo <profile_api/urls.py>, importamos las librerias necesaria
y definimos nuestro router. Y registramos nuestra url de viewset en 
nuestra urlpatterns:

                    ...
            from django.urls import include
            from rest_framework.routers import DefaultRouter

            router = DefaultRouter()
            router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

            urlpatterns = [
                path('hello-view/',views.HelloApiView.as_view()),   
                path('',include(router.urls))
            ]

*******************************************************
3.CREANDO LOS METODOS 
-.---------------------------------------------------.-
nos vamos al archivo <views.py> y definimo nustros serializador
para la clase HelloViewSet:


REVISAR EL VIDEO A PARTIR DE 1:09 

*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-*******************************************************
*******************************************************
*******************************************************
*******************************************************
3.SUPERUSUARIO
-.---------------------------------------------------.-