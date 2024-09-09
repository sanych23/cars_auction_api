# from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Car


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'price', 'year', 'description', 'classification',)

