from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import LoginSerializer

#create yout views here
class IndexView(APIView):
    #para verificar si el usuario esta autenticado
    permissions_classes = (IsAuthenticated)

    def get(self,request):
        context = {'mensaje':'bienbenido a mi api'}
        return Response(context)

class LoginApiView(APIView):

    def post(self,request):
        print(request.data)
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        print(user)
        print(token)
        context = {
            "token":token
        }

        return Response(context)