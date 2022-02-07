from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import AlgorithmType
from .serializers import AlgorithmTypeSerializer


@api_view(['GET'])
def getAlgorithmTypes(request):
    types = AlgorithmType.objects.all()
    serializer = AlgorithmTypeSerializer(types, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAlgorithmType(request, pk):
    types = AlgorithmType.objects.get(id=pk)
    serializer = AlgorithmTypeSerializer(types, many=False)
    return Response(serializer.data)
