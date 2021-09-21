from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

'''vamos a declarar nuestro UserProfileManager, haremos la herenia'''
class UserProfileManager(BaseUserManager):
    """manager para perfiles de usuario, especifica  funciones que sirven para manipular lo que tenemos lo que tenemos dentro del objectos de UserProfile"""

    def create_user(self, email, name, password=None): #la primera funcion para crear ususarios
        """crear nuevo user profile"""
        if not email:                                   #en caso de que no pongan nada en el campo de email en el formulario
            raise ValueError('Ususario debe tener un Email')

        email = self.normalize_email(email)             #lowercase, con esto ponemos todas las mayusculas a minusculas
        user =self.model(email=email, name=name)

        user.set_password(password)                     #el usuario necesita una contraseña
        user.save(using=self._db)                       #le colocamos un hash para un almacenamiento de contraseñas

        return user

    def create_superuser(self, email, name, password):
        """crear un super usuario"""
        user = self.create_user(email,name,password)    #llamamos la funcion de create_user
         
        user.is_superuser = True                        #decimos que nuestros usuario es super ususario
        user.is_staff = True                            #y que es staff
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser,PermissionsMixin):
    """model0 base de datos para ususarios en el sistema"""
    email = models.EmailField(max_length=255, unique=True)  #es uncampo unico que no se puede repetir
    name = models.CharField(max_length=255)  
    is_activate = models.BooleanField(default=True)  #nos dira si el ususario esta activo, o si tiene todo los permisios, esta en tru ay que cada ususario creado estara activo por defecto
    is_staff = models.BooleanField(default=False)   #si son miembros del equipo

    objects = UserProfileManager()  #especificamos el modelManager para nuestros objectos, requerido ayq ue usaremos nuestros modelo de django personalizado
                                    #con el django cli, django necesita un CUSTOM user manager paraq ue django sepa
                                    #como crear , actualizar y borrar usuarios.

    USERNAME_FIELD = 'email'        #campo de login que el usuario va a especificar, ya que haremos login con email y no con usuario
    REQUIRED_FIELDS = ['name']      #colocamos los campos que seran requeridos

    def get_full_name(self):        #definimos funciones que nos permiten llamar nuestro usuarios, cuando queremos ver mediante otra funcion por string
        '''obtener nombre completo'''
        return self.name            
    
    def get_short_name(self):       #de igual manera con esta función
        '''obtener nombre corto'''
        return self.name

    def __str__(self):              #para mostrar la representación de nuestra cadena de texto
        '''retornar cadena representando nuestro usuario'''
        return self.email

