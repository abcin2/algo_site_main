from rest_framework.serializers import ModelSerializer
from .models import AlgorithmType


class AlgorithmTypeSerializer(ModelSerializer):
    class Meta:
        model = AlgorithmType
        fields = '__all__'