from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ serialza un campo para probar nuestra APIVIEW"""
    name = serializers.CharField(max_length=10)

