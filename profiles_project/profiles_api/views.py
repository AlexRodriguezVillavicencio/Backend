from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status #tiene varios codigos http de status que podemos usar como respuesta al usar nuestra api
from profiles_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    ''''API view de prueba'''
    serializer_class = serializers.HelloSerializer  #con esto llamamos a nuestra clase que esta en el archivo serializers.py

    def get(self, request, formart=None):
        '''retornar lstas de caracteristica del APIVIew'''
        an_apiView = [
            'Usamos metodos HTTP com funciones (get, post, patch, put,delete)'
            'es similar a una vista tradicional dn Djando'
            'nos da mayor control sobre la logica de neuestra aplicacion'
            'esta mapeado manualmente a los urls'
        ]

        return Response({'message':'hello','an:apiview': an_apiView})

    def post(self,request):         #agregamos la fucnion post a nuestra apiview
        """crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():           #de ser valido el serializador que le hemos pasado, entonces
            name = serializer.validated_data.get('name') #vamos a poder ver el name, que es el caracter que hemos creado
                                                 #de nuestra clase. Luego de hacer los validated-get queremso obtener el name.
            message = f'hola {name}'
            return Response({'message':message})
        

        else:         # si es que no se cumple, creamos esta opcion
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def put(self,request,pk=None):      #al actulizar tambien se actualiza el ID, por eso le colocamos Pk none para no hacerlo ya que no utilizaremos
                                        # el Id para este ejemplo
        """maneja actualizar un objeto"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """maneja actualizacion parcial de un objeto"""
        return Response({'method': 'PATCH'})

    def delete(self,request,pk=None):
        """borrar un objeto"""
        return Response({'method': 'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """api de testing view set"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """retornar mensaje de hola mundo"""
        a_viewset = [
            'usa acciones (list,create,retrieve, updtae, partial_update'
            'automaticamente mapea a los URL usando routers'
            'provee mas funcionalidades usando menos codigo'
        ]

        return Response({'message':'Hola!','a_viewset':a_viewset})

    def create(self, request):
        """crear nuevo mensaje de hola mundo"""
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

    def retrieve(self,request,pk=None):
        """obtiene un objeto y su ID"""
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        """actualiza un objeto"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """actualiza parcialmente el objeto """
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """elimina el objeto"""
        return Response({'http_method':'DELETE'})

    