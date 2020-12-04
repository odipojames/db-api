from rest_framework import serializers
from .models import *

class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        exclude=('tracking','id')
