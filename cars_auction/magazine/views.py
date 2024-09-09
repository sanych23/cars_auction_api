from django.shortcuts import render
# from django.contrib.auth.models import Group, User
from .models import Car
from rest_framework import permissions, viewsets
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = [permissions.IsAuthenticated]


