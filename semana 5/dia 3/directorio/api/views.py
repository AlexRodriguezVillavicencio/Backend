from rest_framework import APIView
from rest_framework.response import Response

#create yout views here
class IndexView(APIView):

    def get(self,request):
        context = {'mensaje':'bienbenido a mi api'}
        return Response(context)

        