from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    ''''API view de prueba'''

    def get(self, request, formart=None):
        '''retornar lstas de caracteristica del APIVIew'''
        an_apiView = [
            'Usamos metodos HTTP com funciones (get, post, patch, put,delte)'
            'es similar a una vista tradicional dn Djando'
            'nos da mayor control sobre la logica de neuestra aplicacion'
            'esta mapeado manualmente a los urls'
        ]

        return Response({'message':'hello','an:apiview': an_apiView})
