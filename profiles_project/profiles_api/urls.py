from django.urls import path
from profiles_api import views
from django.urls import include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()  #definimos nuestro router
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#el primer argumento es el nombre del url que deseamos crear
#el segundo argumento es el viewset que qeuremos registar
#el tercer argumento es para especificar un nombre base para nuestros viewset

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),    #cargamos la funcion de la clases de views: HelloApuViews
    path('',include(router.urls))
]
