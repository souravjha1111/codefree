from .models import irisModel
from rest_framework import serializers


class irisModelSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = irisModel
        fields = "__all__"